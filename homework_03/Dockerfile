#Execute below command to run docker
#sudo docker run -d --name my_app -p8000:8000 1b75305c5cba

FROM python:3.9-buster


RUN usr/local/bin/python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
COPY ./ ./

CMD uvicorn main:app --host=0.0.0.0




