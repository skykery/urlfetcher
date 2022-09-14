from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse
from starlette_exporter import PrometheusMiddleware, handle_metrics
from services.url import URLService
from models.models import RequestModel, ResponseModel
from starlette.background import BackgroundTask

RAISE_HTTP = True
app = FastAPI(redoc_url=None)
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)


@app.post('/{key}', response_model=ResponseModel)
async def request(key: str, data: RequestModel):

    from services.db import DatabaseService
    user = DatabaseService.get_user(key=key)
    if not user:
        raise HTTPException(status_code=404, detail="A valid api key is required in order to use our services.")

    task = BackgroundTask(DatabaseService.increase_number_of_requests, user_id=user.id)
    try:
        response = URLService.request(data)
    except Exception as e:
        # https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#4xx_Client_errors
        if RAISE_HTTP:
            raise HTTPException(status_code=400, detail=str(e))
        else:
            raise
    return JSONResponse(response, background=task)


from settings import custom_openapi

app.openapi = custom_openapi
