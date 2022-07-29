#!/bin/bash
set -e

sudo docker build -t cr.yandex/crpj02kjhivinp8rg1d9/trista-nudes:$1 .
sudo docker push cr.yandex/crpj02kjhivinp8rg1d9/trista-nudes:$1
