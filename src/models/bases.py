from abc import ABC
from requests.models import Response
from models.models import ResponseDetailsModel


class Backend(ABC):

    def get(self, *args, **kwargs):
        raise NotImplemented

    def post(self, *args, **kwargs):
        raise NotImplemented


class MappedResponseDetails(ResponseDetailsModel):
    def __init__(self, response: Response):
        r = response
        r.history.reverse()
        super().__init__(**dict(
            text=r.text,
            status_code=r.status_code,
            url=r.url,
            history=[response.url for response in r.history],
            elapsed=r.elapsed.total_seconds(),
            reason=r.reason,
            headers=r.headers,
        ))
