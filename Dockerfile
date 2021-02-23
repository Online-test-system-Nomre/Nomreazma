FROM debian
WORKDIR /usr/src/site
#RUN apt-get update -y ; apt-get upgrade -y
RUN apt-get install nginx python3 python3-pip -y ; pip3 install --upgrade pip
COPY . /usr/src/site/
RUN pip3 install -r requirements.txt
RUN python /usr/src/site/manage.py makemigrations; python3 /usr/scr/site/manage.py migrate
RUN python /usr/src/site/manage.py collectstatic --noinput 
RUN uwsgi --http 0.0.0.0:80 --chdir /usr/scr/site/OTSN --wsgi-file /usr/scr/site/OTSN/wsgi.py
RUN uwsgi /usr/src/site/server/nomreazma.ini; cp /usr/scr/site/server/uwsgi.service /etc/systemd/system/
COPY /usr/src/site/server/nginx.conf /etc/nginx/sites-available/nomreazma.conf
RUN ln -s /etc/nginx/sites-available/testproject /etc/nginx/sites-enabled
RUN nginx -t; systemctl enable nginx; systemctl enable uwsgi; ufw allow 'Nginx Full'
