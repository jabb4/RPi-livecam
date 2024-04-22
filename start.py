import subprocess

try:
    startapp_process = subprocess.run(["python","app/manage.py", "runserver", "0.0.0.0:80"])
finally:
    print("exeting")