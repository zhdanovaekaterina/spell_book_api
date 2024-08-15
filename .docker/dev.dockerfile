FROM python:3.11-slim AS compile-image

WORKDIR /code

COPY ./.docker/dev-requirements.txt /tmp/requirements.txt

RUN \
    pip install --upgrade pip && \
    pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r /tmp/requirements.txt

FROM python:3.11-slim AS build-image

RUN useradd --system zhdanova

WORKDIR /code

COPY --from=compile-image /wheels /wheels

RUN \
    pip install --upgrade pip && \
    pip install --no-cache /wheels/*

COPY alembic.ini /code

USER zhdanova

CMD ["uvicorn", "app.rest.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
