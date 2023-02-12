#!/bin/sh
FROM python:3.9-alpine
COPY . /backend
WORKDIR /backend
RUN pip install -r requirements.txt
CMD ["python3", "routes.py"]
