import time
from threading import Thread
from TakeCare import takecare
from CamConstructor import camconstructor
from SendPackage import sendpacket

emergence=True
sendpacket(camconstructor(emergence))


#class sender(Thread):
#    def run(self):
#         while True:
#             time.sleep(0.01)
#             sendpackage(camconstructor(emergence))
#
# class recever(Thread):
#     def run(self):
#         while True:
#             time.sleep(0.01)
#             data = s.recv(1)
#             takecare(data)
# def run():
#     sender.start()
#     recever.start()

# class worker(Thread):
#     def __init__(self):
#         Thread.__init__(self)
#     def run(self):
#         for x in xrange(0, 11):
#             print x
#             time.sleep(1)
#
# class waiter(Thread):
#     def __init__(self):
#         Thread.__init__(self)
#     def run(self):
#         for x in xrange(100, 103):
#             print x
#             time.sleep(5)
#
# def run():
#     worker().start_new_thread()
#     waiter().start_new_thread()