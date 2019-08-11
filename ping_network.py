import socket 
from socket import *
import os
import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import multiprocessing
import subprocess
from multiprocessing import Pool


TIMEOUT = 5 
CONCURRENCY = 100  #pings in parallel

def format_ips(hostnames, ip_list):

    for ip, host in zip(ip_list, hostnames):
        print(ip + " is online " + "(" + host + ")" )
    

def get_hostname(ip_list):

    hostnames = []
    
    for ip in ip_list:
        host = getfqdn(ip)
        hostnames.append(host)

    return hostnames

def ping(ip):

    ret = subprocess.call(['ping ', '-w ', str(TIMEOUT), '-n ', '1 ', ip], stdout=subprocess.DEVNULL)
    if ret == 0:
        return ip

def main():

    ips1 = ("192.168.0." + '%d' % i for i in range(1, 255))
    ips2 = ("192.168.1." + '%d' % i for i in range(1, 255))

    ip_list_main = []
    online_ip_list = []

    p = Pool()
    result = p.map(ping, ips1)

    p.close()
    p.join()

    for val in result:
        if val != None:
            online_ip_list.append(val)

    hostname_list = get_hostname(online_ip_list)
    format_ips(hostname_list, online_ip_list)



if __name__ == "__main__":
    main()