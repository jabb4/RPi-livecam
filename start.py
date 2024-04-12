import subprocess


from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder
from picamera2.outputs import FileOutput

picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main={"size": (640, 480)}))
output = "./app/static/static/images/stream.mjpg"
picam2.start_recording(JpegEncoder(), FileOutput(output))


try:
    startapp_process = subprocess.run(["python","app/manage.py", "runserver"])
finally:
    print("exeting")
    picam2.stop_recording()