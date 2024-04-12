from django.shortcuts import render

from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder
from picamera2.outputs import FileOutput

picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main={"size": (640, 480)}))
output = "stream.mjpg"
picam2.start_recording(JpegEncoder(), FileOutput(output))

# Create your views here.

def stream_view(request):
    
    context = {
        
    }
    return render(request, "stream.html", context=context)