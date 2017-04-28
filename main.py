import time
from CamConstructor import camconstructor
from SendPackage import sendpackage
from TakeCare import takecare

emergence=True
class sender(Thread):
    def run(self):
        while True:
            time.sleep(0.01)
            sendpackage(camconstructor(emergence))

class recever(Thread):
    def run(self):
        while True:
            time.sleep(0.01)
            data = s.recv(1)
            takecare(data)