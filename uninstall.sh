#!/bin/bash

systemctl --user stop cam
systemctl --user stop django

systemctl --user disable cam
systemctl --user disable django

rm ~/.config/systemd/user/django.service
rm ~/.config/systemd/user/cam.service

systemctl --user daemon-reload

echo "now just rm -rf the folder"