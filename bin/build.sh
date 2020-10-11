#!/bin/bash
set -euxo pipefail

cd ..
aws ecr get-login-password --region ap-southeast-2 | docker login --username AWS --password-stdin 542367334738.dkr.ecr.ap-southeast-2.amazonaws.com
docker build -t quanteverest-analytics .
docker tag quanteverest-analytics:latest 542367334738.dkr.ecr.ap-southeast-2.amazonaws.com/quanteverest-analytics:latest
docker push 542367334738.dkr.ecr.ap-southeast-2.amazonaws.com/quanteverest-analytics:latest