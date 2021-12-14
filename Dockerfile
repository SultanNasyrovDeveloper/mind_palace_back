FROM python:3.8-bullseye

# set python specific environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install python dependencies
RUN apt-get update && apt-get upgrade

# install application requirements
RUN mkdir /app
COPY /backend /app
WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT ['python', 'manage.py runserver']