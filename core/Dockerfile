FROM python:3.7-slim

RUN pip install feast[redis]

RUN pip install psycopg2-binary

RUN feast init feature_repo

WORKDIR "./feature_repo"

COPY ./res/feature_store.yaml ./

RUN feast apply