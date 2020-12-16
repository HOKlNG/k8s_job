FROM python:3.6

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY . /k8s_interface

RUN pip install -r /k8s_interface/requirements.txt

RUN chmod 755 /k8s_interface/start

WORKDIR /k8s_interface
EXPOSE 8000

ENTRYPOINT ["/k8s_interface/start"]