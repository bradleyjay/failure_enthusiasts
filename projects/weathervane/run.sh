#!/bin/bash
# import subprocess

# # source env variables
# # subprocess.call('source variables.sh')
# subprocess.Popen(['source ./variables.sh'])

# # subprocess.getstatusoutput('source variables.sh')
# import backend
# print('Imported backend')

source variables.sh
python3 backend.py
