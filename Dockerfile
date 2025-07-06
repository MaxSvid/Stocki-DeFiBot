# Dockerile Image, Container for Bot

# Needed for VPS setup

FROM python13:slim

LABEL maintainer="telegram channel: https://t.me/StockiDeFi_Agent"

ARG UID=1000
ARG GID=1000
ENV UID=${UID}
ENV GID=${GID}

RUN useradd -m -u $UID docker_user

USER docker_user

WORKDIR /home/docker_user/app

ENV key=value

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "-m", "bot.frontdp" ]
