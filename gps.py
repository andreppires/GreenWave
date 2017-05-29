import serial
import re
from sys import platform


def getPosition():

    global latEmisphere
    global latDegrees
    global lonEmisphere
    global lonDegrees
    global utc
    return latEmisphere, latDegrees, lonEmisphere, lonDegrees, utc


def calc_checksum(sentence):
    if re.search("\n$", sentence):
        sentence = sentence[:-1]
    try:
        nmeadata, cksum = re.split('\*', sentence)
    except ValueError:

        return ["0","1","2"]

    nmeadata = nmeadata[1:]
    calc_cksum = 0
    for s in nmeadata:
        calc_cksum ^= ord(s)

    return nmeadata, '0x' + cksum, hex(calc_cksum)


def readgps(sender):
    global latEmisphere
    global latDegrees
    global lonEmisphere
    global lonDegrees
    global utc
    if (sender)==1:
        latEmisphere = 1.000
        latDegrees = 3844.233154296875
        lonEmisphere = 1
        lonDegrees = 918.1594848632812
        utc = 0.000
    else:
        if  (sender)== 2:
            latEmisphere = 1.000
            latDegrees = 3844.0000
            lonEmisphere = 1
            lonDegrees = 918.00000
            utc = 0.000
        else:
            if sender==3:
                latEmisphere = 1.000
                latDegrees = 3800.0000
                lonEmisphere = 1
                lonDegrees = 910.00000
                utc = 0.000
            else:
                latEmisphere = 1.000
                latDegrees = 2.0000
                lonEmisphere = 3.0000
                lonDegrees = 4.0000
                utc = 0.000

    if platform == "linux" or platform == "linux2":
        Ser = serial.Serial(port='/dev/gps0', baudrate=38400, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                            bytesize=serial.EIGHTBITS, timeout=0)
        nmea="/home/andreppires/PycharmProjects/GreenWave/Nmea.txt"
        fnmea="/home/andreppires/PycharmProjects/GreenWave/filtered_nmea.txt"
    elif platform == "win32":
        Ser = serial.Serial(port='COM4', baudrate=38400, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                            bytesize=serial.EIGHTBITS, timeout=0)
        nmea="C:\Users\Pedro\PycharmProjects\GreenWave/Nmea.txt"
        fnmea="C:\Users\Pedro\PycharmProjects\GreenWave/filtered_nmea.txt"

    print("connected to: " + Ser.portstr)
    f = open(nmea, 'w+')
    new_f = open(fnmea, 'w+')

    while True:
        line = Ser.readline()
        if line:
            data, cksum, calc_cksum = calc_checksum(line)
            if int(cksum, 16) == int(calc_cksum, 16):
                with open(nmea, 'a') as f:
                    f.write(line)

                first_split = line.split('*')
                splited = first_split[0].split(',')

                if splited[0] == ('$GPGGA') or splited[0] == ('$GPRMC'):
                    with open(fnmea, 'a') as new_f:
                        new_f.write(line)
                    if splited[0] == ('$GPGGA'):

                        if splited[1] == '':
                            continue
                        utc = float(splited[1])
                        # heading = float(splited[9]) + float(splited[11])

                        if splited[2] == '':
                            continue

                        latDegrees = float(splited[2])  # NOTA: O formato encontra-se em DD.MM.mmmm

                        if splited[3] == '':
                            continue
                        if splited[3] == 'N':  # North = 1 e S=0 (Se sul multiplica-se por -1)
                            latEmisphere = 1.00
                        else:
                            latEmisphere = 0.000

                        if splited[4] == '':
                            continue
                        lonDegrees = float(splited[4])  # NOTA: O formato encontra-se em DD.MM.mmmm

                        if splited[5] == '':
                            continue
                        if splited[5] == 'W':  # East = 1 e West = 0 (Se West multiplica-se por -1)
                            lonEmisphere = 0.000
                        else:
                            lonEmisphere = 1.000

                    if splited[0] == ('$GPRMC'):

                        if splited[1] == '':
                            continue
                        utc = float(splited[1])

                        if splited[3] == '':
                            continue

                        if splited[3] == '':
                            continue
                        latDegrees = float(splited[3])  # NOTA: O formato encontra-se em DD.MM.mmmm

                        if splited[4] == '':
                            continue
                        if splited[4] == 'N':  # North = 1 e S=0 (Se sul multiplica-se por -1)
                            latEmisphere = 1.000
                        else:
                            latEmisphere = 0.000

                        if splited[5] == '':
                            continue
                        lonDegrees = float(splited[5])  # NOTA: O formato encontra-se em DD.MM.mmmm

                        if splited[6] == '':
                            continue
                        if splited[6] == 'W':  # East = 1 e West = 0 (Se West multiplica-se por -1)
                            lonEmisphere = 0.000
                        else:
                            lonEmisphere = 1.0000
        f.close()
    new_f.close()
    Ser.close()


