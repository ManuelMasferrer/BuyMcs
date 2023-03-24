FROM python:3.9.7-slim-buster

COPY requirements.txt /
RUN python3 -m pip install --upgrade pip
RUN pip3 install psycopg2-binary
RUN pip3 install --no-cache-dir -r /requirements.txt

COPY . /BuyMcs
WORKDIR /BuyMcs

EXPOSE 5000
CMD ["/bin/bash"]
ENTRYPOINT gunicorn -w4 -b 0.0.0.0:5000 wsgi:app