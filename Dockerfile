FROM python:3.8-slim-buster

COPY . /var/app/
WORKDIR /var/app/

SHELL ["/bin/bash", "-c"]

RUN apt-get -y update \
    && apt-get install -y gcc \
    && python3.8 -m venv v-env \
    && source v-env/bin/activate \
    && pip3.8 install -r requirements.txt

EXPOSE 5000

CMD source v-env/bin/activate && uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app