import multiprocessing.process
from django.shortcuts import render

import subprocess

def start_stream():
    process = subprocess.run(["python","cameraStream.py"])

def stop_stream():
    process = subprocess.run(["./app/luftpistol/kill_cam.sh"])

def take_pic():
    process = subprocess.run(["python","take_pic.py"])

def stream_view(request):
    try:
        if request.method == "POST" and request.POST["PIC"]:
            stop_stream()
            take_pic()
    except KeyError:
        pass
    
    context = {
        
    }
    return render(request, "stream.html", context=context)

def saved_series_view(request):
    context = {
        
    }
    return render(request, "saved.html", context=context)