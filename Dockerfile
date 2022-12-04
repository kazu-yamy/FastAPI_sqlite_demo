FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt /app/
COPY ./app /app/

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
