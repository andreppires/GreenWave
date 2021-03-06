from geopy.distance import vincenty
import globaldict


def dm(x):
    degrees = int(x) // 100
    minutes = x - 100*degrees

    return degrees, minutes

def decimal_degrees(degrees, minutes):
    return degrees + minutes/60


def calcSentido(latEmisphere, latDegrees, lonEmisphere, lonDegrees, utc, semaphore, sender):



    if latEmisphere == 0:
        latDegrees = decimal_degrees(*dm(latDegrees)) * (-1)
    else:
        latDegrees = decimal_degrees(*dm(latDegrees))
    if lonEmisphere == 0:
        lonDegrees = decimal_degrees(*dm(lonDegrees)) * (-1)
    else:
        lonDegrees = decimal_degrees(*dm(lonDegrees))

    if semaphore[0] == 0:
        latDegrees2 = decimal_degrees(*dm(semaphore[1])) * (-1)
    else:
        latDegrees2 = decimal_degrees(*dm(semaphore[1]))
    if  semaphore[2] == 0:
        lonDegrees2 = decimal_degrees(*dm(semaphore[3])) * (-1)
    else:
        lonDegrees2 = decimal_degrees(*dm(semaphore[3]))

    loc1 = (latDegrees, lonDegrees) # Ambulancia
    loc_sem = (latDegrees2, lonDegrees2) # Este semaforo
    dist1 = vincenty(loc_sem, loc1).miles
    print dist1

    if globaldict.dic_dist[sender] > dist1:  # ele aproxima-se do semaforo
        globaldict.dic_dist[sender] = dist1
        estado = 1
        return estado
    if dist1 > globaldict.dic_dist[sender]:  # ele afasta-se do semaforo
        globaldict.dic_dist[sender] = dist1
        estado = 2
        return estado
    estado = 3
    return estado


def dicCAM(info, sender):
    if float(info[4]) >= float(globaldict.dic_msg[sender][4]):
        globaldict.dic_msg[sender] = info

def cal_closer_semaphore(senderID , dist1):

    if globaldict.dic_msg[0][0] == 0:
        latDegrees = decimal_degrees(*dm(globaldict.dic_msg[0][1])) * (-1)
    else:
        latDegrees = decimal_degrees(*dm(globaldict.dic_msg[0][1]))
    if globaldict.dic_msg[0][2] == 0:
        lonDegrees = decimal_degrees(*dm(globaldict.dic_msg[0][3]))* (-1)
    else:
        lonDegrees = decimal_degrees(*dm(globaldict.dic_msg[0][3]))

    ambulance = (latDegrees, lonDegrees)
    print ambulance
    for key in globaldict.dic_msg:
        if key == senderID or key == 0:
            continue
        if globaldict.dic_msg[key][0] == 0:
            latDegrees2 = decimal_degrees(*dm(globaldict.dic_msg[key][1])) * (-1)
        else:
            latDegrees2 = decimal_degrees(*dm(globaldict.dic_msg[key][1]))
        if globaldict.dic_msg[key][2] == 0:
            lonDegrees2 = decimal_degrees(*dm(globaldict.dic_msg[key][3])) * (-1)
        else:
            lonDegrees2 = decimal_degrees(*dm(globaldict.dic_msg[key][3]))
        other_sem = (latDegrees2, lonDegrees2)

        dist2 = vincenty(ambulance, other_sem).miles
        print 'este e p semaforo' + str(key)
        print dist2
        print 'este e p semaforo' + str(senderID)
        print dist1

        if dist1 > dist2:  # Existe um semaforo mais proximo
            return False

    return True