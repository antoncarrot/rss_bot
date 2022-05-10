FROM python:3.9.12-alpine3.15 as common

RUN apk --no-cache -U upgrade && ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime


FROM common as build

RUN apk add --no-cache build-base libffi-dev && pip3 install poetry

COPY . /app
WORKDIR /app

RUN python3 -m venv venv/ && source venv/bin/activate && poetry install --no-root --no-dev


FROM common

COPY --from=build /app /app

WORKDIR /app

CMD source venv/bin/activate && python -m app
