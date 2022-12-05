FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt /app/
COPY ./app /app/

RUN pip install --no-cache --upgrade pip
RUN pip install --no-cache -r /app/requirements.txt
