# wdocker variables:

#wd# docker = docker
#wd# name = bababsite
#wd# ports = -p 127.0.0.1:8001:8000
#wd# vol = -v $(pwd)/../src:/app

#wd# build = {docker} build -t {name} .
#wd# run = {docker} run -d {ports} {vol} --name {name} {name}

# wdocker commands:

#wd# build: {build}
#wd# run: {run}
#wd# init: {build} && {run}
#wd# shell: {docker} exec -it {name} bash
#wd# start: {docker} start {name}
#wd# stop: {docker} stop {name}
#wd# attach: clear && {docker} attach {name}
#wd# rm: {docker} rm {name}
#wd# ip: echo -n IP: && {docker} exec {name} ip addr | grep 172
#wd# exec: {docker} exec -it {name}

FROM python:3.5
MAINTAINER Benjamin Althues <benjamin@babab.nl>
EXPOSE 8000
RUN mkdir /app
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install gunicorn
CMD gunicorn -b 0.0.0.0:8000 bababsite.wsgi
