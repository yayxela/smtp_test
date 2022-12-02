FROM python:3.9-alpine3.16
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/home/app
RUN mkdir -p $APP_HOME
COPY ./ $APP_HOME

RUN apk update && apk add --no-cache bash

RUN python3 -m pip install --upgrade pip
RUN apk add build-base
RUN pip install -U setuptools pip
RUN pip install -r $APP_HOME/requirements.txt

WORKDIR $APP_HOME
CMD ["uvicorn", "main:app","--reload", "--host", "0.0.0.0", "--port", "8080"]
