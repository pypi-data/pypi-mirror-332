from starlette.exceptions import HTTPException
from typing import Any, Dict, Optional
from typing_extensions import Annotated, Doc
from . import status


class BaseHTTPException(HTTPException):
    """Base class for all HTTP exceptions."""

    def __init__(
        self,
        status_code: int,
        detail: Annotated[
            Any,
            Doc(
                "Any data to be sent to the client in the `detail` key of the JSON response."
            ),
        ] = None,
        headers: Annotated[
            Optional[Dict[str, str]],
            Doc("Any headers to send to the client in the response."),
        ] = None,
    ):
        super().__init__(detail, status_code=status_code, headers=headers)


class BadRequestException(BaseHTTPException):
    """Bad Request (400): The server could not understand the request due to invalid syntax."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_400_BAD_REQUEST)


class UnauthorizedException(BaseHTTPException):
    """Unauthorized (401): The client must authenticate itself to get the requested response."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_401_UNAUTHORIZED)


class ForbiddenException(BaseHTTPException):
    """Forbidden (403): The client does not have access rights to the content."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_403_FORBIDDEN)


class NotFoundException(BaseHTTPException):
    """Not Found (404): The server can not find the requested resource."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_404_NOT_FOUND)


class MethodNotAllowedException(BaseHTTPException):
    """Method Not Allowed (405): The method is not allowed for the requested resource."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_405_METHOD_NOT_ALLOWED)


class NotAcceptableException(BaseHTTPException):
    """Not Acceptable (406): The resource is capable of generating only content not acceptable according to the Accept headers sent in the request."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_406_NOT_ACCEPTABLE)


class ProxyAuthenticationRequiredException(BaseHTTPException):
    """Proxy Authentication Required (407): The client must authenticate itself to use a proxy."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED)


class RequestTimeoutException(BaseHTTPException):
    """Request Timeout (408): The server did not receive a complete request in time."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_408_REQUEST_TIMEOUT)


class ConflictException(BaseHTTPException):
    """Conflict (409): The request could not be completed due to a conflict with the current state of the target resource."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_409_CONFLICT)


class GoneException(BaseHTTPException):
    """Gone (410): The resource requested is no longer available and will not be available again."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_410_GONE)


class LengthRequiredException(BaseHTTPException):
    """Length Required (411): The server refuses to accept the request without a defined content length."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_411_LENGTH_REQUIRED)


class PreconditionFailedException(BaseHTTPException):
    """Precondition Failed (412): The server does not meet one of the preconditions specified by the client in the request headers."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_412_PRECONDITION_FAILED)


class RequestEntityTooLargeException(BaseHTTPException):
    """Request Entity Too Large (413): The server is refusing to process a request because the entity is too large."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)


class RequestUriTooLongException(BaseHTTPException):
    """Request URI Too Long (414): The URI requested by the client is longer than the server is willing to process."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_414_REQUEST_URI_TOO_LONG)


class UnsupportedMediaTypeException(BaseHTTPException):
    """Unsupported Media Type (415): The server refuses to process the request because the media type is not supported."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)


class RequestedRangeNotSatisfiableException(BaseHTTPException):
    """Requested Range Not Satisfiable (416): The range specified by the client in the Range header is invalid."""

    def __init__(self, detail=None, headers=None):
        super().__init__(
            detail, headers, status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
        )


class ExpectationFailedException(BaseHTTPException):
    """Expectation Failed (417): The server cannot meet the requirements of the Expect header."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_417_EXPECTATION_FAILED)


class ImATeapotException(BaseHTTPException):
    """I'm a teapot (418): The server is a teapot and cannot brew coffee."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_418_IM_A_TEAPOT)


class MisdirectedRequestException(BaseHTTPException):
    """Misdirected Request (421): The request was directed at the wrong server."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_421_MISDIRECTED_REQUEST)


class UnprocessableEntityException(BaseHTTPException):
    """Unprocessable Entity (422): The server understands the content type of the request entity, but was unable to process the contained instructions."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_422_UNPROCESSABLE_ENTITY)


class LockedException(BaseHTTPException):
    """Locked (423): The resource that is being accessed is locked."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_423_LOCKED)


class FailedDependencyException(BaseHTTPException):
    """Failed Dependency (424): The request failed due to failure of a previous request."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_424_FAILED_DEPENDENCY)


class UpgradeRequiredException(BaseHTTPException):
    """Upgrade Required (426): The client should switch to a different protocol."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_426_UPGRADE_REQUIRED)


class PreconditionRequiredException(BaseHTTPException):
    """Precondition Required (428): The server requires the request to be conditional."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_428_PRECONDITION_REQUIRED)


class TooManyRequestsException(BaseHTTPException):
    """Too Many Requests (429): The user has sent too many requests in a given amount of time."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_429_TOO_MANY_REQUESTS)


class RequestHeaderFieldsTooLargeException(BaseHTTPException):
    """Request Header Fields Too Large (431): The server refuses to process the request because the header fields are too large."""

    def __init__(self, detail=None, headers=None):
        super().__init__(
            detail, headers, status.HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE
        )


class UnavailableForLegalReasonsException(BaseHTTPException):
    """Unavailable For Legal Reasons (451): The resource is unavailable for legal reasons."""

    def __init__(self, detail=None, headers=None):
        super().__init__(detail, headers, status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)
