import multiprocessing.process
from django.shortcuts import render

from . import models

import subprocess
import time

def start_stream():
    process = subprocess.run(["systemctl", "--user", "start", "cam.service"])

def stop_stream():
    process = subprocess.run(["systemctl", "--user", "stop", "cam.service"])

def take_pic(image_name):
    process = subprocess.run(["python","/home/pi/rasberry-pi-camera-live/camera/take_pic.py", image_name])

def stream_view(request):
    try:
        if request.method == "POST" and request.POST["PIC"]:
            stop_stream()
            time.sleep(1)
            try:
                saved_images = models.saved_images.objects.get(name="default")
                print("Using existing count")
            except:
                saved_images = models.saved_images.objects.create(name="default")
                saved_images.save()
                print("Creating new count")
            saved_images.count += 1
            saved_images.save()
            image_name = f"saved_image_{saved_images.count}"
            print(image_name)
            image = models.image.objects.create(name=f"{image_name}")
            image.save()
            take_pic(image_name)
            start_stream()
    except KeyError:
        pass
    
    context = {
        
    }
    return render(request, "stream.html", context=context)

def saved_series_view(request):

    saved_images = models.image.objects.all()

    context = {
        "saved_images": saved_images
    }
    return render(request, "saved.html", context=context)