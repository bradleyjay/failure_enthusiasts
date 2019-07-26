# Run as a Daemon *** Next Task ** Run Permanantly so that if you restart it will constantly run.

import subprocess

result = subprocess.getstatusoutput('postgrest -D /usr/local/var/postgres/')

if "command not found" in str(result):
    print("error")
    print(subprocess.getstatusoutput('apt install postgresql'))
    subprocess.getstatusoutput('postgres -D /usr/local/var/postgres/')
else:
    subprocess.getstatusoutput('postgres -D /usr/local/var/postgres/')
