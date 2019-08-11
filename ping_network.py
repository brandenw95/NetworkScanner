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
    online_ip_list1 = []
    online_ip_list2 = []

    print("before multithread")
    
    p = Pool()
    result1 = p.map(ping, ips1)
    p.close()
    p.join()

    X = Pool()
    result2 = X.map(ping, ips2)
    X.close()
    X.joint()
    
    print("after map")
    print(result1)
    print("---------------")
    print(result2)
    for val in result1:
        if val != None:
            online_ip_list1.append(val)
    
    for val2 in result2:
        if val != None:
                online_ip_list2.append(val2)

    hostname_list1 = get_hostname(online_ip_list1)
    hostname_list2 = get_hostname(online_ip_list2)
    format_ips(hostname_list1, online_ip_list1)
    print("--------------------------------------")
    format_ips(hostname_list2, online_ip_list2)



if __name__ == "__main__":
    main()