from fastapi import FastAPI
from typing import Any, Dict

app = FastAPI()


@app.get(path="/healthcheck", description="Healthcheck endpoint", tags=["services"])
async def healthcheck() -> Dict[str, Any]:
    """
    Healthcheck endpoint

    Returns:
        Dict[str, Any]: status with value `ok` if the service is up s asdfa sdfasd asfasd fasdf asdf asdfas fas fasf
        asdf asfas fas fasd fas fasf asdf asdfasd f asfas fas fa
    """
    return {
        "status": "ok",
    }
