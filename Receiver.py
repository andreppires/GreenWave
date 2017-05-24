import socket
import struct
from semaforo import calcSentido
from semaforo import dicCAM
import globaldict

from calculaSentido import calcSentido
from AvisaPeoes import avisapeoes
UDP_IP = 'localhost'
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

thisposition=[10, 10]

def receive(senderID):
    if senderID!=0:
        while True:
            data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

            received_data = (struct.unpack('!HHHHHHHfffffH',data))

            emergence=received_data[len(received_data)-1]
            sender= received_data[4-1]

            if(emergence):
                if sender == 0:
                    if globaldict.dic_msg:
                        if len(globaldict.dic_msg[sender]) != 0:
                            if float(globaldict.dic_msg[sender][4]) <= float(received_data[11]):
                                if(calcSentido(received_data[7],received_data[8], received_data[9], received_data[10], received_data[11], globaldict.dic_msg[sender], thisposition)):
                                    print "Ativar estado emergencia!"
                                else:
                                    print "desativar estado de emergencia"
                else:
                    print "Avisar peoes!"
                    avisapeoes(senderID)

            dicCAM(received_data[7:12], sender)



