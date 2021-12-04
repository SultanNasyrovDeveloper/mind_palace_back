FROM python:3.8-bullseye

# set python specific environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install python dependencies
RUN apt-get update

# install application requirements
RUN mkdir /app
COPY /backend /app
COPY backend/docker-app/docker_entrypoint.sh /docker_entrypoint.sh
WORKDIR /app
RUN ls
RUN pip install -r requirements.txt
EXPOSE 8000

ENTRYPOINT ['/bin/sh', 'docker_entrypoint.sh']