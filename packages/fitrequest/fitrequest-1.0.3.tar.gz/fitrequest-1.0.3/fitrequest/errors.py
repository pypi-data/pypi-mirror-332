from dataclasses import dataclass

# https://docs.gunicorn.org/en/stable/settings.html#limit-request-line
LIMIT_REQUEST_LINE = 4094


@dataclass
class FitRequestConfigurationError(ValueError):
    """Base fitrequest configuration error."""


@dataclass
class FitRequestRuntimeError(RuntimeError):
    """Base fitrequest runtime error."""


@dataclass
class UnrecognizedParametersError(FitRequestConfigurationError):
    """
    Unrecognized parameters: the following are neither arguments of the current generated method
    nor valid httpx.request arguments
    """

    method_name: str
    unrecognized_arguments: set[str]


@dataclass
class UrlRequestTooLongError(FitRequestRuntimeError):
    """Triggered when the length of the requested URL exceeds the maximum allowed limit."""

    url: str
    url_size: int
    url_size_limit: int = LIMIT_REQUEST_LINE


@dataclass
class InvalidMethodDecoratorError(FitRequestConfigurationError):
    """
    Exception raised when the specified method decorator is either not a valid callable
    or cannot be retrieved from the global environment using the given name.
    """

    provided_decorator: str


class UnexpectedNoneBaseURLError(FitRequestConfigurationError):
    """Raised when neither MethodConfig nor MethodConfigGroup specifies the base_url attribute."""


class FitDecoratorInvalidUsageError(FitRequestConfigurationError):
    """
    Raised when the @fit decorator is applied to methods that do not belong to a class inheriting from FitRequest.
    """


class MultipleAuthenticationError(FitRequestConfigurationError):
    """
    Raised when more than one authentication method is detected.
    The user should provide only a single valid authentication method for the request.
    """


class HttpVerbNotProvidedError(FitRequestConfigurationError):
    """
    This exception is raised to indicate that a required HTTP verb has not been specified in the
    MethodConfigFamily configuration. The user should ensure that an appropriate HTTP verb
    (such as GET, POST, PUT, PATCH, DELETE) is provided.
    """
