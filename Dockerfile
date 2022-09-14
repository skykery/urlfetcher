FROM python:3.8-alpine
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev openssl-dev build-base &&  apk add --no-cache libxml2-dev libxslt-dev
ADD requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt && apk del .build-deps
ADD src /
CMD [ "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]