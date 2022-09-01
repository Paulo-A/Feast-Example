FROM python:3.7-slim

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

RUN feast init -m feature_repo

WORKDIR "./feature_repo"

COPY ./feature_definitions/ ./

COPY ./res/feature_store.yaml ./
