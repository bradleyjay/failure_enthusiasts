#!/bin/bash
# import subprocess

source variables.sh

python3 create_env.py
#  we're  pretty sure this  THING works
source venv/bin/activate
sleep 5 # figure this THING out later
python3 db_creds.py
python3 backend.py
