from CamConstructor import camconstructor
from SendPackage import sendpacket
def avisapeoes(fromID):
    packet, latEmisphere, latDegrees, lonEmisphere, lonDegrees, utc = camconstructor(True, fromID)
    sendpacket(packet)
   