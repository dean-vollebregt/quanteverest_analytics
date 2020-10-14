FROM python:3.8-slim-buster

COPY . /var/app/
WORKDIR /var/app/

SHELL ["/bin/bash", "-c"]

RUN apt-get -y update \
    && apt-get install -y build-essential cron \
    && python3.8 -m venv v-env \
    && source v-env/bin/activate \
    && pip3.8 install -r requirements.txt

COPY cronjobs /etc/cron.d/cronjobs
RUN crontab /etc/cron.d/cronjobs

CMD service cron start && tail -f /dev/null
