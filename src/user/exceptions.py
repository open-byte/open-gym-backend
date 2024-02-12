from fastapi import status

from core.exceptions.exceptions import APIHTTPException


class UserNotFoundException(APIHTTPException):
    def __init__(self) -> None:
        super().__init__(
            detail='User not found',
            error_code='record_not_found',
            status_code=status.HTTP_404_NOT_FOUND,
        )
