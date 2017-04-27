def camconstructor():
    # header
    protoversion=1 # versão do nosso protocolo
    MessageID= 0 # identificador de cada msg. Tem de ser diferente
    generatiotime=10

    # body
    StatioID=0
    # station caracteristics
    mobileITS= True
    privateITS = True
    PhysicalRelITS = True

    # ReferencePosition

    # latitude
    enumerate latEmisphere = 1 # 1, norte |0, sul
    latDegrees= 0

    # longitude
    enumerate lonEmisphere =1  # 1, norte |0, sul
    lonDegrees = 0

    #Elevation
    elevation = 0 #angulo

    #Heading
    heading = 0 #altura em relação à linha do mar

    #Emergence | Não faz parte das mensagens CAM standard. Evita a necessidade das mensagens DNM
    inEmergence= False #Ambulancia em emergencia? Evita