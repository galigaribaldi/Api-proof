#Image python:3.9.5-slim also works # Image python:3.9.5-slim-buster also works
FROM python:3.8.3-slim

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN python -m pip install --upgrade pip
RUN pip --no-cache-dir install -r requirements.txt

ENTRYPOINT python src/run.py
#CMD ["python", "src/app.py"]