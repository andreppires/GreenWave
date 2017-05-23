import threading
import time
from CamConstructor import camconstructor
from SendPackage import sendpacket
from Receiver import receive
from gps import readgps

emergence=True

class Thread(threading.Thread):
    def __init__(self, t, *args):
        threading.Thread.__init__(self, target=t, args=args)
        self.start()


def sender():
    while True:
        time.sleep(0.01)
        sendpacket(camconstructor(emergence))

def readGPSCoor():
    readgps()

def receiver():
    while True:
        receive()

def main():
    receivee = Thread(receiver)
    gps = Thread(readGPSCoor)
    send = Thread(sender)



if __name__ == '__main__':
    main()