/bin/bash

sudo apt install nginx

sudo rm -rf /etc/nginx/sites-available/default
sudo rm -rf /etc/nginx/sites-enabled/default

sudo cp /home/pi/rasberry-pi-camera-live/nginx_proxy /etc/nginx/sites-avalable/django
sudo ln -s /etc/nginx/sites-avalable/django /etc/nginx/sites-enabled/

sudo systemctl restart nginx