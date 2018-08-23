import subprocess, os, sys
from time import sleep

# 10 jobs is recommended for 4G of RAM

def get_job_count():
    me = subprocess.check_output(['ps aux | grep wapiti | wc -l'], shell=True)
    me = int(me.replace("\n", "")) - 2

    return me

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

urls = []

for line in lines:
    urls.append(line.replace("\n", ""))


for url in urls:
    while True:
        if get_job_count() < int(sys.argv[2]):
            command = './wapiti --color -m backup,blindsql,buster,crlf,delay,exec,file,htaccess,methods,nikto,permanentxss,shellshock,sql,ssrf,xss -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36" -v 2 -u ' + url + "  &"
            print "Executing command: " + command
            os.system(command)
            sleep(2)
            break
        else:
            sleep(5)
