#!/bin/bash
set -euxo pipefail

sudo yum install -y docker
sudo service docker start
sudo docker pull 542367334738.dkr.ecr.ap-southeast-2.amazonaws.com/quanteverest-analytics:latest
sudo docker run -it 542367334738.dkr.ecr.ap-southeast-2.amazonaws.com/quanteverest-analytics:latest /bin/bash