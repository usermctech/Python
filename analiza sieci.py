#!/usr/bin/python
#
# uzycie:
# ./host.py domena
#

import socket, sys # [1]

def getHostIP(domain_name):
    ip_addr = socket.gethostbyname(domain_name) # [2]
    return ip_addr

if __name__ == '__main__':
    domain = sys.argv[1]
print( "Adres IP dla domeny %s to %s" % (domain, getHostIP(domain)))
