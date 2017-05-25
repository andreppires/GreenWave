import struct
import gps


def camconstructor(emergence, senderID):
    # header
    protoversion=1      # versao do nosso protocolo
    MessageID= 0        # identificador de cada msg. Tem de ser diferente - contador ou generation time in milliseconds
    generationtime=10

    # body
    StatioID=senderID          # ambulance=0 | semaforos um outro valor inteiro ainda nao em uso
    # station caracteristics
    if senderID==0:
        mobileITS= True
    else:
        mobileITS=False
    privateITS = True
    PhysicalRelITS = True

    # ReferencePosition

    position=gps.getPosition()
    # latitude
    latEmisphere = position[1-1] # 1, norte |0, sul
    latDegrees= position[2-1]

    # longitude
    lonEmisphere = position[3-1]    # 1, norte |0, sul
    lonDegrees = position[4-1]


    #Heading
    utc = position[5-1]         # altura em relacao a linha do mar
    # Emergence | Nao faz parte das mensagens CAM standard. Evita a necessidade das mensagens DNM
    inEmergence= emergence  # Ambulancia em emergencia
    packet = struct.pack('!HHHHHHHfffffH', protoversion, MessageID, generationtime, StatioID, mobileITS, privateITS,
                         PhysicalRelITS, latEmisphere, latDegrees, lonEmisphere, lonDegrees, utc, inEmergence)

    return packet , latEmisphere, latDegrees, lonEmisphere, lonDegrees, utc