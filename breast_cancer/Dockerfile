FROM python:3.7-slim

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./src

WORKDIR "./src"

CMD [ "python", "./create_dataset.py"]
