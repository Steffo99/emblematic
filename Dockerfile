# TODO: If you're building a library, remove this file!

FROM python:3-alpine AS system
# TODO: Add whatever dependency your image may require
RUN apk add --update build-base python3-dev py-pip musl-dev
RUN pip install "poetry"

FROM system AS workdir
# TODO: Use the name of your project
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
ENTRYPOINT ["poetry", "run", "python", "-m"]
# TODO: Set the name of your Python module
CMD ["emblematic"]

FROM entrypoint AS labels
# TODO: Set a Docker image title
LABEL org.opencontainers.image.title="emblematic"
# TODO: Set a Docker image decription
LABEL org.opencontainers.image.description="Simple icon generator"
# TODO: Set a Docker image license
LABEL org.opencontainers.image.licenses="AGPL-3.0-or-later"
# TODO: Set a Docker image URL
LABEL org.opencontainers.image.url="https://github.com/Steffo99/emblematic/"
# TODO: Set the Docker image authors
LABEL org.opencontainers.image.authors="Stefano Pigozzi <me@steffo.eu>"
