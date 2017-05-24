import threading
import time
from CamConstructor import camconstructor
from SendPackage import sendpacket
from Receiver import receive
from gps import readgps
from button import readButton

emergence=False
senderID=0

class Thread(threading.Thread):
    def __init__(self, t, *args):
        threading.Thread.__init__(self, target=t, args=args)
        self.start()


def sender():
    global emergence
    while True:
        time.sleep(0.01)
        sendpacket(camconstructor(emergence, senderID))


def readGPSCoor():
    readgps()


def receiver():
    while True:
        receive()


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
