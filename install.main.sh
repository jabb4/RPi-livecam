#!/bin/bash

sudo echo 2>/dev/null

if [ ! -d "~/.config/systemd/user/" ]; then
    mkdir -p ~/.config/systemd/user/
fi

cp django.service ~/.config/systemd/user/django.service
cp cam.service ~/.config/systemd/user/cam.service

## Django migrations
/usr/bin/python3 /home/pi/rasberry-pi-camera-live/app/manage.py makemigrations
/usr/bin/python3 /home/pi/rasberry-pi-camera-live/app/manage.py migrate

systemctl --user daemon-reload

loginctl enable-linger pi

systemctl --user enable cam
systemctl --user enable django

systemctl --user start cam
systemctl --user start django

## Nginx
sudo rm -rf /etc/nginx/sites-available/default
sudo rm -rf /etc/nginx/sites-enabled/default

sudo cp /home/pi/rasberry-pi-camera-live/nginx_proxy /etc/nginx/sites-available/django
sudo ln -s /etc/nginx/sites-available/django /etc/nginx/sites-enabled/

sudo systemctl restart nginx

echo "Installation complete!"