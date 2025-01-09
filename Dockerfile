FROM ubuntu:22.04

RUN apt-get update && \
   apt-get install -y python3 python3-pip libgl1 libglib2.0-0 && \
   apt-get clean

WORKDIR /detect_app
COPY ./ultralytics ultralytics
RUN pip3 install ultralytics
COPY ./python/train.py train.py
COPY ./python/val.py val.py
COPY ./python/custom.yaml custom.yaml