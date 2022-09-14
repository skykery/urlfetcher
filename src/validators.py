from models.models import RequestModel
from exceptions import RequestValidationException


class RequestValidators:
    # "proxy": "http://165.22.36.75:8888"
    methods = ['validate_proxy', 'validate_proxies']

    @staticmethod
    def validate_proxy_ip(ip: str):
        import socket
        try:
            socket.inet_aton(ip)
            # legal
        except socket.error:
            raise RequestValidationException("Not a valid format for a proxy.")

    @classmethod
    def validate_proxy(cls, model: RequestModel):
        if model.proxy:
            cls.validate_proxy_ip(model.proxy)

    @classmethod
    def validate_proxies(cls, model: RequestModel):
        for ip in model.proxies:
            cls.validate_proxy_ip(ip)
