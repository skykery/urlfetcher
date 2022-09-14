from enum import Enum
from pydantic import BaseModel
from typing import List, Union, Optional


class Methods(str, Enum):
    GET = 'get'
    POST = 'post'


class CSSSelectorModel(BaseModel):
    selector: Union[str, None] = None
    attr: Union[str, None] = None
    text: bool = False


class RetryModel(BaseModel):
    retries: int = 0
    backoff_multiplier: Optional[int] = 3
    delay: Optional[int] = 2


class CSSSelectorResultModel(CSSSelectorModel):
    results: List[str] = []


class RequestModel(BaseModel):
    # https://fastapi.tiangolo.com/tutorial/schema-extra-example/
    method: Methods = Methods.GET
    url: str = ''
    headers: Optional[dict] = None
    data: Optional[dict] = None
    params: Optional[dict] = None
    timeout: Optional[float] = 120
    proxy: Optional[str] = None
    retry: Optional[RetryModel] = RetryModel()
    # proxies: Optional[List[str]] = []
    css_selectors: Optional[List[CSSSelectorModel]] = []

    class Config:
        schema_extra = {
            "example": {
                "method": "get",
                "url": "https://techwetrust.com",
                "headers": {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"},
                "data": {},
                "params": {},
                "timeout": 10,
                "retry": {"retries": 2, "backoff_multiplier": 3, "delay": 3},
                "css_selectors": [{"selector": "h1", "text": True}, {"selector": "img.avatar", "attr": "src"}],
            }
        }


class ResponseDetailsModel(BaseModel):
    text: Union[str, None] = None
    status_code: Union[None, int] = 0
    url: Union[str, None] = None
    history: Union[List[str], None] = None
    elapsed: float = 0
    reason: Union[str, None] = None
    headers: dict = {}


class ResponseModel(BaseModel):
    # https://fastapi.tiangolo.com/tutorial/response-model/
    response: ResponseDetailsModel
    css_selectors: List[CSSSelectorResultModel] = []
