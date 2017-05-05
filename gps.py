import serial
import re




def calc_checksum(sentence):
    if re.search("\n$", sentence):
        sentence = sentence[:-1]

    nmeadata, cksum = re.split('\*', sentence)

    nmeadata=nmeadata[1:]
    calc_cksum = 0
    for s in nmeadata:
        calc_cksum ^= ord(s)

    return nmeadata, '0x' + cksum, hex(calc_cksum)

def readgps():
    Ser = serial.Serial( port='COM4', baudrate=38400, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)
    print("connected to: " + Ser.portstr)
    f = open('nmea.txt', 'w+')
    new_f = open('filtered_nmea.txt', 'w+')

    emis_lat = 0
    deg_lat = 0

    emis_lon = 0
    deg_lon = 0

    height = 0

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
                        utc=splited[1]
                        height = float(splited[9]) + float(splited[11])
                        deg_lat = float(splited[2]) # NOTA: O formato encontra-se em DD.MM.mmmm
                        if splited[3]=='N': # North = 1 e S=0 (Se sul multiplica-se por -1)
                            emis_lat=1
                        else:
                            emis_lat=0
                        deg_lon = float(splited[4]) # NOTA: O formato encontra-se em DD.MM.mmmm
                        if splited[5] == 'W': # East = 1 e West = 0 (Se West multiplica-se por -1)
                            emis_lon =0
                        else:
                            emis_lon =1

                    if splited[0] == ('$GPRMC'):
                        utc = splited[1]
                        deg_lat = float(splited[3]) # NOTA: O formato encontra-se em DD.MM.mmmm
                        if splited[4] == 'N': # North = 1 e S=0 (Se sul multiplica-se por -1)
                            emis_lat = 1
                        else:
                            emis_lat = 0
                        deg_lon = float(splited[5]) # NOTA: O formato encontra-se em DD.MM.mmmm
                        if splited[6] == 'W': # East = 1 e West = 0 (Se West multiplica-se por -1)
                            emis_lon = 0
                        else:
                            emis_lon = 1

                    print emis_lat, deg_lat , emis_lon , deg_lon , utc , height



    f.close()
    new_f.close()
    Ser.close()

readgps()

