import requests
from models.bases import Backend


class HTTP(Backend):
    extra_options = dict(verify=False)

    @classmethod
    def get(cls, *args, **kwargs):
        return requests.get(*args, **kwargs, **cls.extra_options)

    @classmethod
    def post(cls, *args, **kwargs):
        return requests.post(*args, **kwargs, **cls.extra_options)
