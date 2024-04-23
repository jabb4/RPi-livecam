from picamera2 import Picamera2
from libcamera import controls
import time

picam2 = Picamera2()
capture_config = picam2.create_still_configuration()
### Activate autofocus
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})
picam2.start(show_preview=False)
time.sleep(1)
picam2.switch_mode_and_capture_file(capture_config, "/home/pi/rasberry-pi-camera-live/app/satic/static/images/image.jpg")