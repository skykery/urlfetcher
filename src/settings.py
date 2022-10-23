from fastapi.openapi.utils import get_openapi

DEFAULT_PROXY = "http://rproxy:5566"
DEFAULT_RENDERER = "http://splash:8050"


def add_custom_openapi(app):
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title="UrlWorker",
            version="0.1.0",
            description="",
            routes=app.routes,
        )
        openapi_schema["info"]["x-logo"] = {
            "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
        }
        app.openapi_schema = openapi_schema
        return app.openapi_schema
    app.openapi = custom_openapi
    return app
