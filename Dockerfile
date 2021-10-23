FROM python:3.8-buster

# set python specofic environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install python dependencies
RUN apt update
RUN apt --assume-yes install libpq-dev python-dev
RUN pip install --upgrade pip

# install application requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# run application