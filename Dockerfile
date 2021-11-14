# Author: Pranav H. Deo { phd24@umd.edu }
# Date: 11/13/2021
# Version: v1.0
# Expect Build Time: 2min { Max }

# Any among ubuntu:16.04, ubuntu:18.04 or ubuntu:20.04
FROM ubuntu:20.04
FROM python:3.9

WORKDIR /ArrowStreetCapital

EXPOSE 5000
ENV FLASK_ENV=development
ENV FLASK_APP=WebApp.py

ADD . /ArrowStreetCapital

# Install Dependencies
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN ["apt-get", "update"]
RUN ["apt-get", "-y", "install", "sudo"]

# Run Flask Application
CMD ["flask", "run", "--host", "0.0.0.0"]
