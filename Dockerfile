FROM python:3.8

# set python specific environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=mind_palace.settings

# install python dependencies
RUN apt-get update && apt-get upgrade

# install application requirements
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
