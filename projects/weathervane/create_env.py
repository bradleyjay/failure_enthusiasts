import subprocess

pip_list = subprocess.getstatusoutput('pip3 list')[1]

def verify_install(library):
    is_library_installed = (pip_list.find(library) > 0)

    if not is_library_installed:
        print('installing ' + library)
        subprocess.getstatusoutput('pip3 install ' + library)

# check for postgres and install if not present
result = subprocess.getstatusoutput('postgres -D /usr/local/var/postgres/')

if "command not found" in str(result):
    subprocess.getstatusoutput('apt install postgresql')
    subprocess.getstatusoutput('postgres -D /usr/local/var/postgres/')
else:
    subprocess.getstatusoutput('postgres -D /usr/local/var/postgres/')

verify_install('virtualenv')
#create venv
subprocess.getstatusoutput('python3 -m venv venv')
#activate venv
subprocess.getstatusoutput('. venv/bin/activate')

subprocess.Popen(['venv/bin/pip3', 'install', 'SQLAlchemy'])
subprocess.Popen(['venv/bin/pip3', 'install', 'psycopg2'])
