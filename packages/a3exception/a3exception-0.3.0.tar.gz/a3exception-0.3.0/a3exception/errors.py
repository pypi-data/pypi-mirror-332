# -*- coding: utf-8 -*-


class ErrorType:
    ServerSideError = "ServerSideError"
    ClientSideError = "ClientSideError"


class Error(Exception):
    error_type = None
    message = None

    def __init__(
        self,
        message: str | None = None,
        cause: str | None = None,
        detail: dict | None = None,
        status: str | None = None,
        error_type: str | None = None,
    ):
        self.message = message or self.message
        self.cause = cause
        self.detail = detail
        self.status = status or self.__class__.__name__
        self.error_type = error_type or self.error_type
        assert self.error_type is not None, "error_type must be set."

    def __str__(self):
        return self.message

    def __repr__(self):
        return self.cause


class AuthenticationFailedError(Error):
    error_type = ErrorType.ClientSideError

    def __init__(self, message: str, **kwargs):
        super().__init__(message=message, **kwargs)


class ValidationError(Error):
    error_type = ErrorType.ClientSideError

    def __init__(self, message: str, **kwargs):
        super().__init__(message=message, **kwargs)


class NotFoundError(Error):
    error_type = ErrorType.ClientSideError

    def __init__(self, message: str, **kwargs):
        super().__init__(message=message, **kwargs)


class InvalidTokenError(Error):
    error_type = ErrorType.ClientSideError

    def __init__(self, message: str, **kwargs):
        super().__init__(message=message, **kwargs)


class ForbiddenError(Error):
    error_type = ErrorType.ClientSideError

    def __init__(self, message: str, **kwargs):
        super().__init__(message=message, **kwargs)


class NotAvailableError(Error):
    error_type = ErrorType.ClientSideError

    def __init__(self, message: str, **kwargs):
        super().__init__(message=message, **kwargs)


# client common error below


class ClientKnownError(Error):
    error_type = ErrorType.ClientSideError

    def __init__(self, message: str, **kwargs):
        super().__init__(message=message, **kwargs)


# server common error below


class ServerKnownError(Error):
    error_type = ErrorType.ServerSideError
    message = "A known error has occurred on the service side."

    def __init__(self, cause: str, **kwargs):
        super().__init__(cause=cause, **kwargs)


class ServerUnknownError(Error):
    error_type = ErrorType.ServerSideError
    message = "An unexpected error has occurred on the service side."

    def __init__(self, cause: str, **kwargs):
        super().__init__(cause=cause, **kwargs)
