FROM easypi/alpine-arm
RUN apk update && apk add python3
RUN pip3 install python-telegram-bot

RUN mkdir /soyaya_bot
WORKDIR /soyaya_bot

COPY ./soyaya/* ./soyaya/
CMD python3 soyaya listen
