# md5_sender_to_A.py
# Send the checksum result to computer A

from socket import *
import sys

s = socket(AF_INET,SOCK_DGRAM) # AF_INET = IPV4 , SOCK_DGRAM = UDP
host = '192.168.14.34' # A ip address
port = 9999
buf = 1024 # Maximum bytes to send
addr = (host,port) # Address to send ip + port

# Opens file to read in bytes and sending them to the destination
file_name='md5_from_destination.txt'

s.sendto(file_name,addr)

f=open(file_name,"rb")
data = f.read(buf)
while (data):
    if(s.sendto(data,addr)):
        print "Sending md5 checksum to B..."
        data = f.read(buf)
s.close()
f.close()
