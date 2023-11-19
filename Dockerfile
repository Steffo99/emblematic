FROM python:3-alpine AS system
RUN apk add --update build-base python3-dev py-pip musl-dev
RUN pip install "poetry"

FROM system AS workdir
WORKDIR /usr/src/emblematic

FROM workdir AS dependencies
COPY pyproject.toml ./pyproject.toml
COPY poetry.lock ./poetry.lock
RUN poetry install --no-root --no-dev

FROM dependencies AS package
COPY . .
RUN poetry install

FROM package AS entrypoint
ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["poetry", "run", "python", "-m", "emblematic"]
CMD []

FROM entrypoint AS labels
LABEL org.opencontainers.image.title="emblematic"
LABEL org.opencontainers.image.description="Generate emblems from an icon and a background"
LABEL org.opencontainers.image.licenses="AGPL-3.0-or-later"
LABEL org.opencontainers.image.url="https://github.com/Steffo99/emblematic/"
LABEL org.opencontainers.image.authors="Stefano Pigozzi <me@steffo.eu>"
