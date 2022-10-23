import requests
from models.bases import Backend, MappedHTTPResponseDetails
from settings import DEFAULT_RENDERER


class Browser(Backend):
    extra_options = dict(verify=False)
    render_url = f'{DEFAULT_RENDERER}/render.html'

    @classmethod
    def get(cls, *args, **kwargs):
        response = requests.get(
            cls.render_url,
            params=dict(url=kwargs['url'],
                        proxy=kwargs['proxies']['http'],
                        timeout=kwargs['timeout'])
        )
        return MappedHTTPResponseDetails(response)

    @classmethod
    def post(cls, *args, **kwargs):
        pass
