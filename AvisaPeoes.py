from CamConstructor import camconstructor
from SendPackage import sendpacket
import globaldict
def avisapeoes(fromID):
    packet, latEmisphere, latDegrees, lonEmisphere, lonDegrees, utc = camconstructor(globaldict.emergence, fromID)
    sendpacket(packet)
   