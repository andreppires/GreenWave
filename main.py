import threading
import time
import globaldict
from CamConstructor import camconstructor
from SendPackage import sendpacket
from Receiver import receive
from gps import readgps
from button import readButton
from semaforo import dicCAM
from NormalLED import LEDS

senderID = 0


class Thread(threading.Thread):
    def __init__(self, t, *args):
        threading.Thread.__init__(self, target=t, args=args)
        self.start()


def sender():
    globaldict.dic_msg = {}
    while True:
        time.sleep(1)
        packet, latEmisphere, latDegrees, lonEmisphere, lonDegrees, utc = camconstructor(globaldict.emergence, senderID)
        dicCAM([latEmisphere, latDegrees, lonEmisphere, lonDegrees, utc, ], senderID)
        # print latEmisphere, latDegrees, lonEmisphere, lonDegrees, utc
        sendpacket(packet)


def readGPSCoor():
    global senderID
    readgps(senderID)


def leds():
    global senderID
    if senderID != 0:
        LEDS()


def receiver():
    global senderID
    receive(senderID)


def Button():
    # Por razoes de teste nao estou a restringir esta thread as ambulancias
    while True:
        globaldict.emergence = readButton()


def main():
    receivee = Thread(receiver)
    gps = Thread(readGPSCoor)
    send = Thread(sender)
    btn = Thread(Button)
    leeeeeds=Thread(leds)

if __name__ == '__main__':
    main()
