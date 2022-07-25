FROM python:3.9-alpine
WORKDIR /usr/src/scraping
COPY ./app ./app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt