#!/bin/bash

# First putt service files in the right folder

cp django.service ~/.config/systemd/user/django.service
cp cam.service ~/.config/systemd/user/cam.service

systemctl --user daemon-reload

systemctl --user enable cam.service
systemctl --user enable django.service

systemctl --user start cam.service
systemctl --user start django.service