from fastapi.exceptions import HTTPException


class APIHTTPException(HTTPException):
    def __init__(self, detail: str, error_code: str, status_code: int) -> None:
        error = {
            'code': error_code,
            'description': detail,
        }
        super().__init__(status_code=status_code, detail=error)
