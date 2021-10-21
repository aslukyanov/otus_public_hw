#Execute below command to run docker
#sudo docker run -d --name my_app -p8000:8000 <image ID>

FROM python:3.9-buster

WORKDIR /var/app/
COPY ./requirements.txt ./requirements.txt
RUN /usr/local/bin/python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
#COPY ./ ./

COPY ./main.py ./main.py
COPY ./shed.py ./shed.py

RUN mkdir ./template

COPY ./template/page.html ./template/page.html
COPY ./template/page2.html ./template/page2.html

CMD uvicorn main:app --host=0.0.0.0




