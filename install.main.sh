#!/bin/bash

pip install -r /home/pi/rasberry-pi-camera-live/requirements.txt

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

chmod +x uninstall.sh
chmod +x install.nginx.sh

./install.nginx.sh