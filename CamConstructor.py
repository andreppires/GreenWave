import struct
import gps

def camconstructor(emergence):
    # header
    protoversion=1      # versao do nosso protocolo
    MessageID= 0        # identificador de cada msg. Tem de ser diferente - contador ou generation time in milliseconds
    generationtime=10

    # body
    StatioID=0          # ambulance=0 | semaforos um outro valor inteiro ainda nao em uso
    # station caracteristics
    mobileITS= True
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

    #Elevation
    elevation = 0       # angulo

    #Heading
    utc = position[5-1]         # altura em relacao a linha do mar

    # Emergence | Nao faz parte das mensagens CAM standard. Evita a necessidade das mensagens DNM
    inEmergence= emergence  # Ambulancia em emergencia

    packet = struct.pack('!HHHHHHHHHHHHHH', protoversion, MessageID, generationtime, StatioID, mobileITS, privateITS,
                         PhysicalRelITS, latEmisphere, latDegrees, lonEmisphere, lonDegrees, elevation, utc, inEmergence)
    print packet
    return packet

camconstructor(1)