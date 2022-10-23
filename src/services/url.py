import logging
from requests.models import Response
from backends.browser import Browser
from backends.http import HTTP
from models.models import RequestModel, ResponseModel, Backends
from parsers.html import HTMLParser
from utils.decorators import retry
from utils.request import RequestUtils
from validators import RequestValidators

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class URLService(object):
    backends = {
        Backends.HTTP: HTTP,
        Backends.BROWSER: Browser,
    }
    utils = RequestUtils
    validators = RequestValidators

    @classmethod
    def request(cls, model: RequestModel):
        @retry(
            Exception,
            retries=model.retry.retries,
            backoff_multiplier=model.retry.backoff_multiplier,
            delay=model.retry.delay
        )
        def get_response(_backend, _model):
            return getattr(_backend, _model.method.value)(
                url=_model.url,
                headers=_model.headers,
                data=_model.data,
                params=_model.params,
                timeout=_model.timeout,
                proxies=_model.proxy,
            )

        # TODO: fix validators, make them more generic
        # for validator in cls.validators.methods:
        #     getattr(cls.validators, validator)(model)

        for method in cls.utils.methods:
            getattr(cls.utils, method)(model)

        backend = cls.backends[model.backend]
        logger.info(model)
        response: Response = get_response(_backend=backend, _model=model)

        mapped_response = ResponseModel(response=response)
        mapped_response.css_selectors = HTMLParser(text=mapped_response.response.text).get_css_results(model=model)

        logger.info(mapped_response)
        return mapped_response.dict()
