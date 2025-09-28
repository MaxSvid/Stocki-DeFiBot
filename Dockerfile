# Used light Python image
FROM python:3.12-slim

LABEL maintainer="Telegram bot: https://t.me/StockiDeFi_bot"
LABEL author="Max Svid"
LABEL version="1.0"
LABEL description="Tg bot for Stocki"

# Create non-root user
ARG UID=1000
ARG GID=1000
ENV UID=${UID}
ENV GID=${GID}

RUN useradd -m -u $UID docker_user

USER docker_user

# Set working directory to the bot folder 
# In Linux it starts with /home 
WORKDIR /home/docker_user/app

# Python settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy and install dependencies
# This file depends on docker-compose to copy .env 
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy the project
COPY . .

# Run bot from the bot directory
CMD ["python3", "bot/main.py"]