#!/bin/bash
# import subprocess

source variables.sh

python3 create_env.py
#  we're  pretty sure this  THING works

sleep 5 # figure this THING out later

source venv/bin/activate

sleep 5 # figure this THING out later

python3 flask_app_skeleton.py
