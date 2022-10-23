import requests
from models.bases import Backend, MappedHTTPResponseDetails


class HTTP(Backend):
    extra_options = dict(verify=False)

    @classmethod
    def get(cls, *args, **kwargs):
        response = requests.get(*args, **kwargs, **cls.extra_options)
        return MappedHTTPResponseDetails(response)

    @classmethod
    def post(cls, *args, **kwargs):
        response = requests.post(*args, **kwargs, **cls.extra_options)
        return MappedHTTPResponseDetails(response)
