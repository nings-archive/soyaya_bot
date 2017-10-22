FROM easypi/alpine-arm
RUN apk update && apk add python3

RUN mkdir /soyaya
WORKDIR /soyaya

COPY requirements.txt .
RUN pip3 install python-telegram-bot

COPY keys.py .
COPY soyaya.py .
CMD ./soyaya.py
