import multiprocessing.process
from django.shortcuts import render

import subprocess

def start_stream():
    process = subprocess.run(["python","cameraStream.py"])

def stop_stream():
    process = subprocess.run(["./app/luftpistol/kill_cam.sh"])

def take_pic():
    pass

def stream_view(request):
    if request.method == "POST":
        print(request)
    
    context = {
        
    }
    return render(request, "stream.html", context=context)

def saved_series_view(request):
    context = {
        
    }
    return render(request, "saved.html", context=context)