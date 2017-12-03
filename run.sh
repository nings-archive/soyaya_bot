#!/usr/bin/env bash

docker container rm soyaya
docker run -d --name soyaya -v $(pwd)/volume:/soyaya_bot/volume soyaya
