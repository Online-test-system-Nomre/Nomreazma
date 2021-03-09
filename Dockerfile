FROM python:3.8-slim
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y nginx supervisor build-essential gcc libc-dev libffi-dev default-libmysqlclient-dev libpq-dev
RUN pip install --upgrade pip
RUN pip install gunicorn
COPY ./src /usr/src/app/
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
RUN mkdir -p /etc/uwsgi/sites
COPY config/nomreazma /etc/nginx/sites-available/nomreazma
RUN chmod +x config/run; ./config/run
