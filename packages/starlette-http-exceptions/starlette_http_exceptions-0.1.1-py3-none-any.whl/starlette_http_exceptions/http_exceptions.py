from starlette.exceptions import HTTPException as StarletteHTTPException
from typing import Any, Dict, Optional
from typing_extensions import Annotated, Doc
from . import status


class HTTPException(StarletteHTTPException):
    """
    An HTTP exception you can raise in your own code to show errors to the client.

    This is for client errors, invalid authentication, invalid data, etc. Not for server
    errors in your code.
    """

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


class BadRequestException(StarletteHTTPException):
    """Bad Request (400): The server could not understand the request due to invalid syntax."""

    def __init__(
        self,
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
        super().__init__(
            detail, status_code=status.HTTP_400_BAD_REQUEST, headers=headers
        )


class UnauthorizedException(StarletteHTTPException):
    """Unauthorized (401): The client must authenticate itself to get the requested response."""

    def __init__(
        self,
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
        super().__init__(
            detail, status_code=status.HTTP_401_UNAUTHORIZED, headers=headers
        )


class ForbiddenException(StarletteHTTPException):
    """Forbidden (403): The client does not have access rights to the content."""

    def __init__(
        self,
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
        super().__init__(detail, status_code=status.HTTP_403_FORBIDDEN, headers=headers)


class NotFoundException(StarletteHTTPException):
    """Not Found (404): The server can not find the requested resource."""

    def __init__(
        self,
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
        super().__init__(detail, status_code=status.HTTP_404_NOT_FOUND, headers=headers)


class MethodNotAllowedException(StarletteHTTPException):
    """Method Not Allowed (405): The method is not allowed for the requested resource."""

    def __init__(
        self,
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
        super().__init__(
            detail, status_code=status.HTTP_405_METHOD_NOT_ALLOWED, headers=headers
        )


class NotAcceptableException(StarletteHTTPException):
    """Not Acceptable (406): The resource is capable of generating only content not acceptable according to the Accept headers sent in the request."""

    def __init__(
        self,
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
        super().__init__(
            detail, status_code=status.HTTP_406_NOT_ACCEPTABLE, headers=headers
        )


class ProxyAuthenticationRequiredException(StarletteHTTPException):
    """Proxy Authentication Required (407): The client must authenticate itself to use a proxy."""

    def __init__(
        self,
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
        super().__init__(
            detail,
            status_code=status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED,
            headers=headers,
        )


class RequestTimeoutException(StarletteHTTPException):
    """Request Timeout (408): The server did not receive a complete request in time."""

    def __init__(
        self,
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
        super().__init__(
            detail, status_code=status.HTTP_408_REQUEST_TIMEOUT, headers=headers
        )


class ConflictException(StarletteHTTPException):
    """Conflict (409): The request could not be completed due to a conflict with the current state of the target resource."""

    def __init__(
        self,
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
        super().__init__(detail, status_code=status.HTTP_409_CONFLICT, headers=headers)


class GoneException(StarletteHTTPException):
    """Gone (410): The resource requested is no longer available and will not be available again."""

    def __init__(
        self,
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
        super().__init__(detail, status_code=status.HTTP_410_GONE, headers=headers)


class LengthRequiredException(StarletteHTTPException):
    """Length Required (411): The server refuses to accept the request without a defined content length."""

    def __init__(
        self,
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
        super().__init__(
            detail, status_code=status.HTTP_411_LENGTH_REQUIRED, headers=headers
        )


class PreconditionFailedException(StarletteHTTPException):
    """Precondition Failed (412): The server does not meet one of the preconditions specified by the client in the request headers."""

    def __init__(
        self,
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
        super().__init__(
            detail, status_code=status.HTTP_412_PRECONDITION_FAILED, headers=headers
        )


class RequestEntityTooLargeException(StarletteHTTPException):
    """Request Entity Too Large (413): The server is refusing to process a request because the entity is too large."""

    def __init__(
        self,
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
        super().__init__(
            detail,
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            headers=headers,
        )


class RequestUriTooLongException(StarletteHTTPException):
    """Request URI Too Long (414): The URI requested by the client is longer than the server is willing to process."""

    def __init__(
        self,
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
        super().__init__(
            detail, status_code=status.HTTP_414_REQUEST_URI_TOO_LONG, headers=headers
        )


class UnsupportedMediaTypeException(StarletteHTTPException):
    """Unsupported Media Type (415): The server refuses to process the request because the media type is not supported."""

    def __init__(
        self,
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
        super().__init__(
            detail, status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, headers=headers
        )


class RequestedRangeNotSatisfiableException(StarletteHTTPException):
    """Requested Range Not Satisfiable (416): The range specified by the client in the Range header is invalid."""

    def __init__(
        self,
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
        super().__init__(
            detail,
            status_code=status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE,
            headers=headers,
        )


class ExpectationFailedException(StarletteHTTPException):
    """Expectation Failed (417): The server cannot meet the requirements of the Expect header."""

    def __init__(
        self,
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
        super().__init__(
            detail, status_code=status.HTTP_417_EXPECTATION_FAILED, headers=headers
        )


class ImATeapotException(StarletteHTTPException):
    """I'm a teapot (418): The server is a teapot and cannot brew coffee."""

    def __init__(
        self,
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
        super().__init__(
            detail, status_code=status.HTTP_418_IM_A_TEAPOT, headers=headers
        )


class MisdirectedRequestException(StarletteHTTPException):
    """Misdirected Request (421): The request was directed at the wrong server."""

    def __init__(
        self,
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
        super().__init__(
            detail, status_code=status.HTTP_421_MISDIRECTED_REQUEST, headers=headers
        )


class UnprocessableEntityException(StarletteHTTPException):
    """Unprocessable Entity (422): The server understands the content type of the request entity, but was unable to process the contained instructions."""

    def __init__(
        self,
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
        super().__init__(
            detail, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, headers=headers
        )


class LockedException(StarletteHTTPException):
    """Locked (423): The resource that is being accessed is locked."""

    def __init__(
        self,
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
        super().__init__(detail, status_code=status.HTTP_423_LOCKED, headers=headers)


class FailedDependencyException(StarletteHTTPException):
    """Failed Dependency (424): The request failed due to failure of a previous request."""

    def __init__(
        self,
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
        super().__init__(
            detail, status_code=status.HTTP_424_FAILED_DEPENDENCY, headers=headers
        )


class UpgradeRequiredException(StarletteHTTPException):
    """Upgrade Required (426): The client should switch to a different protocol."""

    def __init__(
        self,
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
        super().__init__(
            detail, status_code=status.HTTP_426_UPGRADE_REQUIRED, headers=headers
        )


class PreconditionRequiredException(StarletteHTTPException):
    """Precondition Required (428): The server requires the request to be conditional."""

    def __init__(
        self,
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
        super().__init__(
            detail, status_code=status.HTTP_428_PRECONDITION_REQUIRED, headers=headers
        )


class TooManyRequestsException(StarletteHTTPException):
    """Too Many Requests (429): The user has sent too many requests in a given amount of time."""

    def __init__(
        self,
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
        super().__init__(
            detail, status_code=status.HTTP_429_TOO_MANY_REQUESTS, headers=headers
        )


class RequestHeaderFieldsTooLargeException(StarletteHTTPException):
    """Request Header Fields Too Large (431): The server refuses to process the request because the header fields are too large."""

    def __init__(
        self,
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
        super().__init__(
            detail,
            status_code=status.HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE,
            headers=headers,
        )


class UnavailableForLegalReasonsException(StarletteHTTPException):
    """Unavailable For Legal Reasons (451): The resource is unavailable for legal reasons."""

    def __init__(
        self,
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
        super().__init__(
            detail,
            status_code=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS,
            headers=headers,
        )
