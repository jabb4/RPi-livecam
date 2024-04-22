import subprocess

try:
    startapp_process2 = subprocess.run(["python","app/luftpistol/cameraStream.py"])
    startapp_process = subprocess.run(["python","app/manage.py", "runserver", "0.0.0.0:8080"])
finally:
    print("exeting")