import socket
import struct
from calculaSentido import calcSentido
UDP_IP = 'localhost'
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

def receive():
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

        received_data = (struct.unpack('!HHHHHHHfffffH',data))
        print received_data
        emergence=received_data[len(received_data)-1]
        sender= received_data[4-1]
        print "senderP= "+str(sender)

        if(emergence):
            if sender == 0:
                if(calcSentido(received_data[7],received_data[8], received_data[9], received_data[10], received_data[11])):
                    print "Ativar estado emergencia!"
                else:
                    print "desativar estado de emergencia"
            else:
                print "Avisar peoes!"
        else:
            if sender == 0:
                print "Saber o sentido do movimento da Ambulancia!"
                calcSentido(received_data[7], received_data[8], received_data[9], received_data[10], received_data[11])
            else:
                print "Alerta! Mau comportamento"



