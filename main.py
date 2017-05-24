import threading
import time
from CamConstructor import camconstructor
from SendPackage import sendpacket
from Receiver import receive
from gps import readgps
from button import readButton
import globaldict
from semaforo import dicCAM

emergence=True
senderID=1

class Thread(threading.Thread):
    def __init__(self, t, *args):
        threading.Thread.__init__(self, target=t, args=args)
        self.start()


def sender():
    global emergence
    globaldict.dic_msg = {}
    while True:
        time.sleep(0.01)
        packet ,latEmisphere, latDegrees, lonEmisphere, lonDegrees, utc= camconstructor(emergence, senderID)
        dicCAM([latEmisphere, latDegrees, lonEmisphere, lonDegrees, utc,], senderID )
        sendpacket(packet)




def readGPSCoor():
    readgps()


def receiver():
    global senderID
    while True:
        receive(senderID)


def Button():
    global emergence
    while True:
        emergence = readButton()


def main():
    receivee = Thread(receiver)
    gps = Thread(readGPSCoor)
    send = Thread(sender)
    btn = Thread(Button)


if __name__ == '__main__':
    main()
