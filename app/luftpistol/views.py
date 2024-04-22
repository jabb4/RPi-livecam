import multiprocessing.process
from django.shortcuts import render

import subprocess

def start_stream():
    process = subprocess.run(["python","cameraStream.py"])

def stop_stream():
    process = subprocess.run(["./kill_cam.sh"])

def take_pic():
    pass

def stream_view(request):
    stop_stream()
    
    context = {
        
    }
    return render(request, "stream.html", context=context)