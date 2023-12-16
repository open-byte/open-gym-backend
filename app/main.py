from typing import (
    Any,
    Dict,
)

from fastapi import (
    FastAPI,
)

app = FastAPI()


@app.get(path='/healthcheck', description='Healthcheck endpoint', tags=['services'])
async def healthCheck() -> Dict[str, Any]:
    """
    Esto es un healthcheck
    (quiero texto duymmy,
    quiero texto duymmy
    quiero texto duymmy quiero texto duymmy,
    quiero texto duymmy,
    quiero texto duymmy quiero texto ,duymmy quiero texto duymmy quiero texto duymmy,)
    """
    caseMinor = 1
    caseMinor += 1
    caseMinor += 1
    return {'status': 'ok'}
