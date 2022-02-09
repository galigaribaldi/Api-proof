#Image python:3.9.5-slim also works # Image python:3.9.5-slim-buster also works
FROM python:3.8.3-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN python -m pip install --upgrade pip
RUN pip --no-cache-dir install -r requirements.txt

#ENTRYPOINT python src/run.py
#CMD ["python", "src/app.py"]
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 --chdir src run:app