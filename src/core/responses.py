from typing import Any

from fastapi.responses import JSONResponse


class CJSONResponse(JSONResponse):
    """
    This is a custom JSON response class for all API endpoints.
    """

    def __init__(self, content: dict[Any, Any], status_code: int = 200, **kwargs: Any) -> None:
        """
        This is a custom JSON response class for all API endpoints.

        Args:
            content (dict, optional): Response content. Defaults to None.
            status_code (int, optional): HTTP status code. Defaults to 200.
        """
        if isinstance(content, dict):
            status_code = content.pop('status_code', status_code)

        super().__init__(content=content, status_code=status_code, **kwargs)
