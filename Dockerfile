FROM python:3.8-slim
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y nginx supervisor build-essential gcc libc-dev libffi-dev default-libmysqlclient-dev libpq-dev
RUN pip install --upgrade pip
RUN pip install gunicorn
COPY . /usr/src/app/
RUN if [ ! -f requirements.txt ]; then echo requirements.txt does not exist >&2; exit 1; fi; 
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["sh", "/usr/src/app/run.sh"]
