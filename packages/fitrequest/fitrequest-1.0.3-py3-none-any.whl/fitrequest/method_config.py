import logging
from enum import Enum
from functools import cached_property
from typing import Any

import httpx
import jinja2
import jinja2.meta
from pydantic import BaseModel, ConfigDict, Field, model_validator
from typing_extensions import Self

from fitrequest.errors import (
    LIMIT_REQUEST_LINE,
    UnexpectedNoneBaseURLError,
    UrlRequestTooLongError,
)
from fitrequest.fit_var import ValidFitVar
from fitrequest.method_decorator import ValidMethodDecorator
from fitrequest.utils import extract_method_params, format_url, string_varnames

logger = logging.getLogger(__name__)


class RequestVerb(str, Enum):
    delete = 'DELETE'
    get = 'GET'
    patch = 'PATCH'
    post = 'POST'
    put = 'PUT'


class MethodConfig(BaseModel):
    """Describes the configuration of ONE method. No the other method is declared: Explicit is better than implicit."""

    # method vars
    name: str
    """Name of the method that will be created."""

    save_method: bool = False
    """Boolean indicating if the method includes an extra argument ``filepath`` to write the response to a file."""

    async_method: bool = False
    """Boolean indicating whether the generated method is asynchronous."""

    docstring: str = ''
    """
    Jinja template for the generated method (overrides default).
    The default variable declaration ``{{my_var}}`` is replaced by ``{my_var}``.
    See: https://jinja.palletsprojects.com/en/stable/
    """

    docstring_vars: dict[Any, Any] = Field(default_factory=dict)
    """Values of the docstring variables."""

    decorators: list[ValidMethodDecorator] = Field(default_factory=list)
    """Decorators applied to the generated method."""

    # url vars
    base_url: ValidFitVar = None
    """Base URL for the generated method (overrides default)."""

    endpoint: str
    """Endpoint of the request."""

    # request vars
    raise_for_status: bool = True
    """Whether to raise an exception for response status codes between 400 and 599."""

    request_verb: RequestVerb = RequestVerb.get
    """HTTP verb for the request, defined in the RequestVerb enumeration."""

    json_path: str | None = None
    """
    JSON path string used to extract data from the received JSON response.
    See: https://pypi.org/project/jsonpath-ng/
    """

    data_model: type[BaseModel] | None = None
    """Pydantic model used to format the request's response."""

    model_config = ConfigDict(extra='forbid', validate_default=True)

    @property
    def docstring_varnames(self) -> set[str]:
        return string_varnames(self.jinja_env, self.docstring)

    @property
    def endpoint_varnames(self) -> set[str]:
        return string_varnames(self.jinja_env, self.endpoint)

    @property
    def signature(self) -> str:
        endpoint_params = [f'{arg}: str' for arg in self.endpoint_varnames]
        request_params = [f'raise_for_status: bool = {self.raise_for_status}', '**kwargs']
        save_params = ['filepath: str'] if self.save_method else []
        signature_params = ', '.join(['self', *endpoint_params, *save_params, *request_params])
        return_type = 'None' if self.save_method else 'Any'
        return f'{self.name}({signature_params}) -> {return_type}'

    @cached_property
    def jinja_env(self) -> jinja2.Environment:
        return jinja2.Environment(
            variable_start_string='{',
            variable_end_string='}',
            autoescape=True,  # ruff S701
        )

    @cached_property
    def url_template(self) -> jinja2.Template:
        return self.jinja_env.from_string(f'{self.base_url}/{self.endpoint}'.lstrip('/'))

    @cached_property
    def docstring_template(self) -> jinja2.Template:
        return self.jinja_env.from_string(self.docstring)

    @model_validator(mode='after')
    def validate_doctring(self) -> Self:
        if self.docstring_varnames:
            docstring_env = self.model_dump(exclude={'docstring_vars'}) | self.docstring_vars
            self.docstring = self.docstring_template.render(**docstring_env)
        return self

    def url(self, **kwargs) -> str:
        if self.base_url is None:
            raise UnexpectedNoneBaseURLError

        url = format_url(self.url_template.render(**kwargs))
        httpx_params = extract_method_params(httpx.request, kwargs)
        final_url = str(httpx.Request(method=self.request_verb, url=url, **httpx_params).url)

        if len(final_url) > LIMIT_REQUEST_LINE:
            raise UrlRequestTooLongError(url=final_url, url_size=len(final_url))
        return url
