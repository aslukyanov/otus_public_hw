FROM python:3.9-buster

COPY ./ ./
RUN usr/local/bin/python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt


CMD uvicorn main:app --host=0.0.0.0




