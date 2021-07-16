# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.7-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Set current directory as ENV
ENV PATH=/app:$PATH

# copy items
WORKDIR /app
COPY src/main.py ./
COPY src/requirements.txt ./

# Install pre-dependencies
RUN apt update
RUN apt install -y wget g++ unzip xvfb

# install python dependencies
RUN pip install -r requirements.txt

# Install chrome
RUN wget http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_91.0.4472.101-1_amd64.deb
RUN apt install -y ./google-chrome-stable_91.0.4472.101-1_amd64.deb

# Download chromedriver
RUN wget https://chromedriver.storage.googleapis.com/91.0.4472.101/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
