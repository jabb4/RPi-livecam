#!/bin/bash

# First putt service files in the right folder

cp django.service /etc/systemd/system/django.service
cp cam.service /etc/systemd/system/cam.service

systemctl daemon-reload

systemctl enable cam.service
systemctl enable django.service

systemctl start cam.service
systemctl start django.service