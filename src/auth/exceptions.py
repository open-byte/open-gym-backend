from fastapi import status

from core.exceptions.exceptions import APIHTTPException


class JWTInvalidCredentials(APIHTTPException):
    def __init__(self) -> None:
        super().__init__(
            detail='Invalid credentials provided.',
            error_code='invalid_credentials',
            status_code=status.HTTP_401_UNAUTHORIZED,
        )


class JWTNoAuthorizationAccess(APIHTTPException):
    def __init__(self) -> None:
        super().__init__(
            detail='You are not authorized to access this resource.',
            error_code='invalid_token',
            status_code=status.HTTP_401_UNAUTHORIZED,
        )


class JWTUnknownError(APIHTTPException):
    def __init__(self) -> None:
        super().__init__(
            detail='An unknown error occurred while processing the JWT token.',
            error_code='jwt_unknown_error',
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


class JWTUserInactive(APIHTTPException):
    def __init__(self) -> None:
        super().__init__(
            detail='Your account is inactive.',
            error_code='jwt_user_inactive',
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
