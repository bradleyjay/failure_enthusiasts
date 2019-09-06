import subprocess


# Prep Postgres, start postgres
mac = True
if not mac:            # I'm hilarious
    subprocess.getstatusoutput('apt install postgresql')
    subprocess.getstatusoutput('postgres -D /usr/local/var/postgres/')

# Check for Python3 and Pip3
logs = []
if "pip3" not in subprocess.getstatusoutput('which pip3')[1]:
    logs.append('Please install pip3 before continuing!')

if "python3" not in subprocess.getstatusoutput('which python3')[1]:
    logs.append('Please install python3 before continuing!')

if logs:
    for i in logs:
        print(str(i))
    quit()

print('Pip3 and Python3 detected.')

# No errors? create venv
subprocess.getstatusoutput('python3 -m venv venv')

subprocess.Popen(['venv/bin/pip3', 'install', '-r', 'requirements.txt'])
subprocess.Popen(['.', 'venv/bin/activate'])
