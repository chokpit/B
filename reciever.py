# receiver.py
# Listening on UDP port 9999 in order to recieve a file.

from socket import *
import sys
import select

host = "192.168.14.92" # B ip address 
port = 9999
s = socket(AF_INET,SOCK_DGRAM) # AF_INET = IPV4, SOCK_DGRAM = UDP
s.bind((host,port)) # Bind the socket to an address
addr = (host,port)

buf = 1024
data,addr = s.recvfrom(buf) # Recieve data from the socket
print "Received File:",data.strip()
fname = data.strip()
f = open(data.strip(),'wb')

data,addr = s.recvfrom(buf)
try:
    while(data):
        f.write(data)
        s.settimeout(2) 
        data,addr = s.recvfrom(buf)
except timeout:
    f.close()
    s.close() # Set socket timeout of 2 seconds
    print "File Downloaded"
    sys.argv = ['md5_check.py', fname]
    execfile('md5_check.py')
    execfile('md5_sender_to_A.py')
