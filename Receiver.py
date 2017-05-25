import socket
import struct
from semaforo import calcSentido
from semaforo import dicCAM
import globaldict
import threading
from NormalLED import normalLED
from NormalLED import emergenceLED
import psutil

from AvisaPeoes import avisapeoes
UDP_IP = 'localhost'
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

thisposition=[3844.233154296875, 918.1594848632812]



def receive(senderID, ledsEmNormal):

    #if senderID!=0:

        while True:
            data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

            received_data = (struct.unpack('!HHHHHHHfffffH',data))
            emergence=received_data[len(received_data)-1]
            sender= received_data[4-1]

            if(emergence):
                if sender == 0:
                    if globaldict.dic_msg:
                        if len(globaldict.dic_msg[sender]) != 0:
                            if float(globaldict.dic_msg[sender][4]) < float(received_data[11]):
                                estado=(calcSentido(received_data[7], received_data[8], received_data[9], received_data[10],
                                             received_data[11], thisposition, sender))
                                if estado==1:
                                    ledsEmNormal.kill()
                                    ledsEmEmergencia = psutil.Process(emergenceLED)
                                    ledsEmEmergencia.start()
                                    print "Ativar estado emergencia!"
                                if estado==2:
                                    ledsEmEmergencia.kill()
                                    ledsEmNormal = psutil.Process(normalLED)
                                    ledsEmNormal.start()
                                    print "desativar estado de emergencia"
                                if estado==3:
                                    print 'Mantem Estado Anterior'
                else:
                    print "Avisar peoes!"
                    avisapeoes(senderID)
            print globaldict.dic_dist
            dicCAM(received_data[7:12], sender)



