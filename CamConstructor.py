def camconstructor(emergence):
    # header
    protoversion=1      # versao do nosso protocolo
    MessageID= 0        # identificador de cada msg. Tem de ser diferente - contador ou generation time in milliseconds
    generatiotime=10

    # body
    StatioID=0          # ambulance=0 | semaforos um outro valor inteiro ainda nao em uso
    # station caracteristics
    mobileITS= True
    privateITS = True
    PhysicalRelITS = True

    # ReferencePosition

    # latitude
    latEmisphere = 1    # 1, norte |0, sul
    latDegrees= 0

    # longitude
    lonEmisphere = 1    # 1, norte |0, sul
    lonDegrees = 0

    #Elevation
    elevation = 0       # angulo

    #Heading
    heading = 0         # altura em relacao a linha do mar

    # Emergence | Nao faz parte das mensagens CAM standard. Evita a necessidade das mensagens DNM
    inEmergence= emergence  # Ambulancia em emergencia

    packet=
    return 0
