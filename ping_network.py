import socket 
from socket import *
import os
import platform   
import subprocess  
import multiprocessing
import subprocess
from multiprocessing import Pool
import wmi


TIMEOUT = 5 
CONCURRENCY = 100  

def format_ips(hostnames, ip_list):

    
    for ip, host in zip(ip_list, hostnames):
        print(ip + " is online " + "(" + host + ")" )
    print("-------------------------------------------------")
    
def grab_domain():

    domain = []

    wmiobj = wmiobj()
    

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

def pool(ip):
    
    p = Pool()
    result = p.map(ping, ip)
    p.close()
    p.join()

    return result

def refine(ip_list):
    
    refined_list = []

    for val in ip_list:
        if val != None:
            refined_list.append(val)

    return refined_list

def main():

    ips1 = ("192.168.0." + '%d' % i for i in range(1, 255))
    ips2 = ("192.168.1." + '%d' % i for i in range(1, 255))

    ip_list_main = []
    online_ip_list1 = []
    online_ip_list2 = []
    
    result1 = pool(ips1)
    result2 = pool(ips2)
    
    online_ip_list1 = refine(result1)
    online_ip_list2 = refine(result2)

    hostname_list1 = get_hostname(online_ip_list1)
    hostname_list2 = get_hostname(online_ip_list2)

    format_ips(hostname_list1, online_ip_list1)
    format_ips(hostname_list2, online_ip_list2)



if __name__ == "__main__":
    main()