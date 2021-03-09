#!/bin/sh
ln -s /etc/nginx/sites-available/nomreazma /etc/nginx/sites-available/
nginx -t
systemctl restart nginx
systemctl start uwsgi
systemctl enable nginx
systemctl enable uwsgi