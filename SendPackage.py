import socket

def sendpacket(packet):
    UDP_IP = "localhost"
    UDP_PORT = 5005
    MESSAGE = packet

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    return



