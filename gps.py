import serial


def readgps():
    Ser = serial.Serial( port='COM3', baudrate=38400, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)
    print("connected to: " + Ser.portstr)
    filename = open('nmea.txt', 'w')

    while True:
        line = Ser.readline()
        mystr = str(line, 'utf-8')
        filename.write(mystr)
        filename.write("\n")
        if line:
            print(line)
    filename.close()
    Ser.close()

readgps()