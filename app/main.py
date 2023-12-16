from fastapi import FastAPI

app = FastAPI()


@app.get(path='/healthcheck', description='Healthcheck endpoint', tags=['services'])
async def healthcheck() -> dict[str, str]:
    return {
        'status': 'ok',
    }
