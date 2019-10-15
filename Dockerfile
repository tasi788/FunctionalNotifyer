FROM python:3.7 as builder

ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update \
    && apt-get install openssl \
    && apt-get install ca-certificates
WORKDIR /app
COPY ./bot/requirements.txt .
RUN pip install -r requirements.txt

FROM builder
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]
