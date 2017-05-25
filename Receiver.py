import socket
import struct
import globaldict
from semaforo import calcSentido
from semaforo import dicCAM
from AvisaPeoes import avisapeoes

UDP_IP = ''
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

thisPosition = [3844.233154296875, 918.1594848632812]


def receive(senderID):
    if senderID != 0:
        while True:
            data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
            received_data = (struct.unpack('!HHHHHHHfffffH', data))
            localEmergence = received_data[len(received_data) - 1]
            sender = received_data[4-1]
            print "Sender recebido= "+str(sender)

            if (localEmergence):
                if sender == 0:
                    if globaldict.dic_msg:
                        if len(globaldict.dic_msg[sender]) != 0:
                            # if float(globaldict.dic_msg[sender][4]) < float(received_data[11]):
                            estado = (
                                calcSentido(received_data[7], received_data[8], received_data[9], received_data[10],
                                            received_data[11], thisPosition, sender))
                            # TODO falta verificar se este semaforo e o mais proximo da ambulancia.
                            if estado == 1:
                                globaldict.emergence = True
                                avisapeoes(senderID)
                                print "Ativar estado emergencia!"
                                print "Avisar peoes!"
                            if estado == 2:
                                globaldict.emergence = False
                                print "desativar estado de emergencia"
                            if estado == 3:
                                print 'Mantem Estado Anterior'
            print globaldict.dic_dist
        dicCAM(received_data[7:12], sender)
        print globaldict.dic_msg
