FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/base
COPY requirements.txt ./
RUN pip3 install -r requirements.txt