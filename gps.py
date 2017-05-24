import serial
import re


def getPosition():

    global latEmisphere
    global latDegrees
    global lonEmisphere
    global lonDegrees
    global utc
    #print latEmisphere, latDegrees, lonEmisphere, lonDegrees, utc
    return latEmisphere, latDegrees, lonEmisphere, lonDegrees, utc


def calc_checksum(sentence):
    if re.search("\n$", sentence):
        sentence = sentence[:-1]

    nmeadata, cksum = re.split('\*', sentence)

    nmeadata = nmeadata[1:]
    calc_cksum = 0
    for s in nmeadata:
        calc_cksum ^= ord(s)

    return nmeadata, '0x' + cksum, hex(calc_cksum)


def readgps():
    global latEmisphere
    latEmisphere = 1.000
    global latDegrees
    latDegrees = 2.0000
    global lonEmisphere
    lonEmisphere = 3.0000
    global lonDegrees
    lonDegrees = 4.0000
    global utc
    utc = 0.000

    Ser = serial.Serial(port='COM3', baudrate=38400, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS, timeout=0)

    print("connected to: " + Ser.portstr)
    f = open('nmea.txt', 'w+')
    new_f = open('filtered_nmea.txt', 'w+')

    while True:
        line = Ser.readline()
        if line:
            data, cksum, calc_cksum = calc_checksum(line)
            if int(cksum, 16) == int(calc_cksum, 16):
                with open("C:\Users\Pedro\PycharmProjects\GreenWave/Nmea.txt", 'a') as f:
                    f.write(line)

                first_split = line.split('*')
                splited = first_split[0].split(',')

                if splited[0] == ('$GPGGA') or splited[0] == ('$GPRMC'):
                    with open("C:\Users\Pedro\PycharmProjects\GreenWave/filtered_nmea.txt", 'a') as new_f:
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


