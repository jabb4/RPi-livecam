import multiprocessing.process
from django.shortcuts import render

import multiprocessing
from . import cameraStream

# Create your views here.
stream = multiprocessing.process(target=cameraStream.run_stream, args=())
stream.start()

def take_pic():
    pass

def stream_view(request):
    
    context = {
        
    }
    return render(request, "stream.html", context=context)