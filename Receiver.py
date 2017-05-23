import socket
import struct
UDP_IP = "255.255.255.255"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

def receive():
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        received_data = (struct.unpack('!HHHHHHHHHHHHHH',data))
        print received_data
        emergence=received_data[len(received_data)-1]
        if(emergence):
            print "emergencia!"
        else:
            print "nooot"



