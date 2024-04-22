#!/bin/bash

kill $(ps -ef | grep "cameraStream.py" | head -n 1 | awk '{print $2}')