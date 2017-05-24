from geopy.distance import vincenty
import globaldict

def calcSentido(latEmisphere, latDegrees, lonEmisphere, lonDegrees, utc, laststate, semaphore):
    if latEmisphere == 0:
        latDegrees=latDegrees*(-1)
    if lonEmisphere == 0:
        lonDegrees=lonDegrees*(-1)

    if laststate[1] == 0:
        lastlat=laststate[0]*(-1)
    else:
        lastlat=laststate[0]
    if laststate[3] == 0:
        lastlon=laststate[2]*(-1)
    else:
        lastlon = laststate[2]

    loc1=(latDegrees, lonDegrees)
    loc2=(lastlat, lastlon)
    loc_sem=(semaphore[0], semaphore[1])

    dist1=vincenty(loc_sem, loc1).miles
    dist2=vincenty(loc_sem, loc2).miles

    if dist2>=dist1: # ele aproxima-se do semaforo
        return True
    if dist1>dist2: # ele afasta-se do semaforo
        dist1 > dist2
        return False

def dicCAM(info, sender):

    if globaldict.dic_msg:
        if len(globaldict.dic_msg[sender])!=0:
            if float(info[4]) < float(globaldict.dic_msg[sender][4]):
                return globaldict.dic_msg
            else:
                globaldict.dic_msg[sender]=info
        else:
            globaldict.dic_msg[sender] = info
    else:
        globaldict.dic_msg[sender]=info
    return

