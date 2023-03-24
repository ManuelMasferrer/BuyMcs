FROM python:3.9.7-slim-buster

RUN apt-get update \
    && apt-get -y install libpq-dev gcc 

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install --no-cache-dir -r /app/requirements.txt
COPY . /app

EXPOSE 5000
CMD ["/bin/bash"]
ENTRYPOINT gunicorn -w4 -b 0.0.0.0:5000 app:app
