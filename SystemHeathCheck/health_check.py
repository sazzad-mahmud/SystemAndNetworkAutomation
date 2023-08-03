#!/usr/bin/env python3
import shutil
import psutil
import socket
import requests


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total*100
    return free < 20


def check_cpu_usage():
    cu = psutil.cpu_percent(1)
    return cu > 75

# checks whether the local host is correctly configured. We do this by calling the gethostbyname within the function.

#The bellow check_localhost function translates a host name to IPv4 address format. Pass the parameter localhost to the function gethostbyname. The result for this function should be 127.0.0.1.


def check_localhost():
    localhost =socket.gethostbyname("localhost")
    return localhost == '127.0.0.1'

#A request is when you ping a website for information. The Requests library is designed for this task. You will use the request module for this, and call the GET method by passing http://www.google.com as the parameter.

def check_connectivity():
    request = requests.get("http://www.google.com")
    response = request.status_code
    return response == 200

#status_code is a function of request module. It returns 200 or 404. 200 means connectivity is ok. 404 menas error.


if check_disk_usage("/home") or check_cpu_usage():
    print("ERROR!")

elif not check_localhost() or not check_connectivity():
    print("Network Error!")

else:
    print("Everything is OK!")


