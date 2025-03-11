import inspect
import re
from collections.abc import Callable
from urllib.parse import parse_qs, urlparse

import jinja2
import jinja2.meta


def extract_method_params(method: Callable, params: dict) -> dict:
    """Return the parameters used in 'method' found in 'kwargs'."""
    return {field: value for field, value in params.items() if field in inspect.signature(method).parameters}


def format_url(url: str) -> str:
    """Format url to remove redundant / character."""
    return re.sub(r'/+', '/', url).replace(':/', '://')


def string_varnames(jinja_env: jinja2.Environment, template: str) -> set[str]:
    """Extract named variables from template."""
    return jinja2.meta.find_undeclared_variables(jinja_env.parse(template))


def extract_url_params(url: str | None) -> tuple[str | None, dict]:
    """Extract url parameters and return the base url and it's parameters as dict."""
    if not url:
        return None, {}
    parsed_url = urlparse(url)
    scheme = parsed_url.scheme + '://' if parsed_url.scheme else ''

    base_url = scheme + parsed_url.netloc + parsed_url.path
    params = parse_qs(parsed_url.query)

    return base_url, params
