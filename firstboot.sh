#!/bin/bash

# First putt service files in the right folder

systemctl daemon-reload

systemctl enable cam.service
systemctl enable django.service

systemctl start cam.service
systemctl start django.service