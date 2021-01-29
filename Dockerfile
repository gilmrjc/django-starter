FROM alpine AS templates

WORKDIR /usr/src/app/

COPY backend backend

RUN find backend \! -name "*.html" -type f -print | tr "\n" "\0" | xargs -0 rm

FROM node:12-alpine AS assets

WORKDIR /usr/src/app

COPY lerna.json package.json package-lock.json ./

RUN npm install

COPY frontend frontend

RUN npm run bootstrap

COPY --from=templates /usr/src/app/backend backend

RUN npm run build

FROM python:3.8-alpine

ARG INCLUDE_DEV_DEPENDENCIES

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN apk add --no-cache --virtual .build-deps \
      build-base python3-dev cargo libressl-dev libffi-dev \
    && pip install pdm \
    && apk del .build-deps

COPY pyproject.toml pdm.lock ./

RUN apk add --no-cache --virtual .build-deps \
      build-base cargo libressl-dev libffi-dev \
      postgresql-dev \
      jpeg-dev zlib-dev \
    && pdm sync \
    && if [ ! -z "$INCLUDE_DEV_DEPENDENCIES" ]; then pdm sync --dev; fi \
    && runDeps="$(scanelf --needed --nobanner --recursive __pypackages__ \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && echo "Libraries dependencies: $runDeps" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps

COPY gunicorn.conf.py .

COPY backend backend

COPY --from=assets /usr/src/app/backend/assets backend/assets

EXPOSE 8000

WORKDIR /usr/src/app/backend

ENTRYPOINT ["./entrypoint.sh"]

CMD ["gunicorn", "-c", "/usr/src/app/gunicorn.conf.py", "core.wsgi:application"]
