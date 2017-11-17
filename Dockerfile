FROM easypi/alpine-arm
RUN apk update && apk add python3
RUN pip3 install python-telegram-bot

RUN mkdir /soyaya
WORKDIR /soyaya

COPY *.py ./
CMD ./soyaya.py
