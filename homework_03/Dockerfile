FROM python:3.9-buster

RUN mkdir /home/app
COPY ./ /home/app
RUN usr/local/bin/python3 -m pip install --upgrade pip
RUN pip3 install -r /home/app/requirements.txt


CMD uvicorn main:app --host=0.0.0.0




