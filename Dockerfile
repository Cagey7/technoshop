FROM python:3.10.5-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . .

RUN chmod +x /code/entrypoint.sh

CMD [ "/code/entrypoint.sh" ]
