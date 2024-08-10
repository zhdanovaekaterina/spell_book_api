FROM python:3.12-slim AS compile-image

WORKDIR /code

COPY ./.docker/requirements.txt /tmp

RUN \
    pip install --upgrade pip && \
    pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r /tmp/requirements.txt

FROM python:3.12-slim AS build-image

RUN useradd --system zhdanova

WORKDIR /code

COPY --from=compile-image /wheels /wheels

RUN \
    pip install --upgrade pip && \
    pip install --no-cache /wheels/*

RUN \
    mkdir ./.pytest_cache && \
    chown zhdanova ./.pytest_cache

USER zhdanova

CMD ["pytest", "-vs"]
