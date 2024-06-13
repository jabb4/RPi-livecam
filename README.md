## Stream video live from your Raspberry Pi

RPi-livecam is a program to stream a video from a raspberry-pi cam and to host a webpage to be able to view and interact with the streamed video. This program consists of three services runing simuztanisly. Python webpage that host the streamed video, django (gunicorn) webpage that the user interacts with and finaly a nignx service that handels static files. This project was initially built to be used for an air pistol range to easily view and digitally save scores live, but it can also be used for other purposes.

### Tested hardware

- [Raspberry Pi Zero 2 W](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/) with [Raspberry Pi Camera Module 3](https://www.raspberrypi.com/products/camera-module-3/)


### Features

-   Stream video from raspberrypi to webpage
-   Access stream from all devices on the same network
-   Save and view images from the stream in the webpage UI

### Installation

1.   Install dependecies

```
sudo apt install python3-pip python3-picamera2 git nginx
```

2.  Clone repo

```
git clone && cd RPi-livecam
```

3.  Install pip requerments

```
pip install -r requierments.txt --break-system-packages
```

4.  Change www-data in /etc/nginx/nginx.conf to your defualt username for your Pi

```
sudo nano /etc/nginx/nginx.conf
```

5.  Run installation script

```
chmod +x install.sh && ./install.sh
```

6. Done, you can now vissit your livecam at <your-RPi-ip-adress\>:80

### Demo
- Coming soon