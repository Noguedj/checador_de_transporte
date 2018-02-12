#!/usr/bin
while 1 == 1:
    import subprocess, time
    hosts = ("8.8.8.8", "yahoo.com")
    def ping(host):
        ret = subprocess.call(["ping", "-c", "3", "-w", "5", host],
            stdout = open("/dev/null", "w"),
            stderr = open("/dev/null", "w"))
        return ret == 0
    print ("checando red")
    xstatus = 1
    if ping("8.8.8.8"):
        q = true
        xstatus = 0
    if xstatus:
        q = false
    
    
    
