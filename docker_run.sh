#!/usr/bin/env bash

docker run -d --name soyaya -v $(pwd)/volume:/soyaya/volume soyaya
