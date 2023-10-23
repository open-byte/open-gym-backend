# standard library imports
from typing import Any, Dict

# third party imports
from fastapi import FastAPI

app = FastAPI()


@app.get(
    "/healthcheck",
    description="Healthcheck endpoint",
    tags=["services"],
)
async def healthcheck() -> Dict[
    str,
    Any,
]:
    """
    Healthcheck endpoint

    Returns:
        Dict[str, Any]: status with value `ok` if the service is up    asdfa sdfasd asfasd fasdf asdf asdfas fas fasf
        asdf asfas fas fasd fas fasf asdf asdfasd f asfas fas fa
    """
    return {
        "status": "ok",
    }
