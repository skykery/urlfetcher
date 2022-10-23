from models.models import RequestModel
from settings import DEFAULT_PROXY


class RequestUtils:
    methods = [
        'add_default_proxy',
        'clean_string_from_lists',
        'request_proxy_on_model',
        # 'proxies_to_request_proxies'
    ]

    @staticmethod
    def add_default_proxy(model: RequestModel):
        if not model.proxy:
            model.proxy = DEFAULT_PROXY

    @staticmethod
    def proxy_string_to_request_proxy(proxy):
        return dict(http=proxy, https=proxy)

    @classmethod
    def request_proxy_on_model(cls, model: RequestModel):
        if model.proxy:
            model.proxy = cls.proxy_string_to_request_proxy(model.proxy)

    @classmethod
    def proxies_to_request_proxies(cls, model: RequestModel):
        if model.proxies:
            model.proxies = [cls.proxy_string_to_request_proxy(proxy) for proxy in model.proxies]

    @staticmethod
    def clean_string_from_lists(model: RequestModel):
        for key in model.dict().keys():
            field = getattr(model, key)
            if isinstance(field, list):
                try:
                    field.remove('string')
                except ValueError:
                    pass
