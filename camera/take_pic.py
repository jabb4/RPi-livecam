from picamera2 import Picamera2
from libcamera import controls
import time
import sys

image_name = sys.argv[1]

picam2 = Picamera2()
capture_config = picam2.create_still_configuration(main={"size": (1000, 1000)})
picam2.start(show_preview=False)
### Activate autofocus
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})
time.sleep(1)
picam2.switch_mode_and_capture_file(capture_config, f"/home/pi/rasberry-pi-camera-live/app/static/static/images/{image_name}.jpg")