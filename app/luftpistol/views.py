import multiprocessing.process
from django.shortcuts import render

import multiprocessing
import subprocess
from . import cameraStream

def run_stream():
    process = subprocess.run(["python","cameraStream.py"])

stream = multiprocessing.process(target=run_stream(), args=())
stream.start()

def stream_view(request):
    
    context = {
        
    }
    return render(request, "stream.html", context=context)