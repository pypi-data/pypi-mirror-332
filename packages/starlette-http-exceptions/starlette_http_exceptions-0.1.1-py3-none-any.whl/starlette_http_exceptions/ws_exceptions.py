from typing import Annotated, Union
from starlette.exceptions import WebSocketException as StarletteWebSocketException
from typing_extensions import Doc
from . import status


class WebSocketException(StarletteWebSocketException):
    """
    A WebSocket exception you can raise in your own code to show errors to the client.

    This is for client errors, invalid authentication, invalid data, etc. Not for server
    errors in your code.
    """

    def __init__(
        self,
        code: Annotated[
            int,
            Doc(
                """
                A closing code from the
                [valid codes defined in the specification](https://datatracker.ietf.org/doc/html/rfc6455#section-7.4.1).
                """
            ),
        ],
        reason: Annotated[
            Union[str, None],
            Doc(
                """
                The reason to close the WebSocket connection.

                It is UTF-8-encoded data. The interpretation of the reason is up to the
                application, it is not specified by the WebSocket specification.

                It could contain text that could be human-readable or interpretable
                by the client code, etc.
                """
            ),
        ] = None,
    ) -> None:
        super().__init__(code=code, reason=reason)


class WSProtocolError(WebSocketException):
    """Protocol Error (1002): The connection was closed due to a protocol error."""

    def __init__(self, reason=None):
        super().__init__(code=status.WS_1002_PROTOCOL_ERROR, reason=reason)


class WSUnsupportedData(WebSocketException):
    """Unsupported Data (1003): The connection was closed due to unsupported data."""

    def __init__(self, reason=None):
        super().__init__(code=status.WS_1003_UNSUPPORTED_DATA, reason=reason)


class WSNoStatusReceived(WebSocketException):
    """No Status Received (1005): No status code was received."""

    def __init__(self, reason=None):
        super().__init__(code=status.WS_1005_NO_STATUS_RCVD, reason=reason)


class WSAbnormalClosure(WebSocketException):
    """Abnormal Closure (1006): The connection was closed abnormally."""

    def __init__(self, reason=None):
        super().__init__(code=status.WS_1006_ABNORMAL_CLOSURE, reason=reason)


class WSInvalidFramePayloadData(WebSocketException):
    """Invalid Frame Payload Data (1007): Invalid frame payload data."""

    def __init__(self, reason=None):
        super().__init__(code=status.WS_1007_INVALID_FRAME_PAYLOAD_DATA, reason=reason)


class WSPolicyViolation(WebSocketException):
    """Policy Violation (1008): The connection was closed due to a policy violation."""

    def __init__(self, reason=None):
        super().__init__(code=status.WS_1008_POLICY_VIOLATION, reason=reason)


class WSMessageTooBig(WebSocketException):
    """Message Too Big (1009): The connection was closed due to a message being too big."""

    def __init__(self, reason=None):
        super().__init__(code=status.WS_1009_MESSAGE_TOO_BIG, reason=reason)


class WSMandatoryExt(WebSocketException):
    """Mandatory Extension (1010): The connection was closed because a mandatory extension was expected."""

    def __init__(self, reason=None):
        super().__init__(code=status.WS_1010_MANDATORY_EXT, reason=reason)


class WSInternalError(WebSocketException):
    """Internal Error (1011): The connection was closed due to an internal server error."""

    def __init__(self, reason=None):
        super().__init__(code=status.WS_1011_INTERNAL_ERROR, reason=reason)


class WSServiceRestart(WebSocketException):
    """Service Restart (1012): The connection was closed due to a service restart."""

    def __init__(self, reason=None):
        super().__init__(code=status.WS_1012_SERVICE_RESTART, reason=reason)


class WSTryAgainLater(WebSocketException):
    """Try Again Later (1013): The connection was closed with the suggestion to try again later."""

    def __init__(self, reason=None):
        super().__init__(code=status.WS_1013_TRY_AGAIN_LATER, reason=reason)


class WSBadGateway(WebSocketException):
    """Bad Gateway (1014): The connection was closed due to a bad gateway error."""

    def __init__(self, reason=None):
        super().__init__(code=status.WS_1014_BAD_GATEWAY, reason=reason)


class WSTLSHandshake(WebSocketException):
    """TLS Handshake (1015): The connection was closed due to a TLS handshake error."""

    def __init__(self, reason=None):
        super().__init__(code=status.WS_1015_TLS_HANDSHAKE, reason=reason)
