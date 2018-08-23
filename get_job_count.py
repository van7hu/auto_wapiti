import subprocess, os, sys
from time import sleep

def get_job_count():
    me = subprocess.check_output(['ps aux | grep wapiti | wc -l'], shell=True)
    me = int(me.replace("\n", "")) - 2

    return me

while True:
    print "Number of jobs running: " + str(get_job_count())
    sleep(5)
