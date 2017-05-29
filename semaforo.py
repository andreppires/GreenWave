from geopy.distance import vincenty
import globaldict

def calcSentido(latEmisphere, latDegrees, lonEmisphere, lonDegrees, utc, semaphore, sender):



    if latEmisphere == 0:
        latDegrees = latDegrees * (-1)
    if lonEmisphere == 0:
        lonDegrees = lonDegrees * (-1)

    if semaphore[0] == 0:
        latDegrees2 = semaphore[1] * (-1)
    else:
        latDegrees2 = semaphore[1]
    if  semaphore[2] == 0:
        lonDegrees2 = semaphore[3] * (-1)
    else:
        lonDegrees2 = semaphore[3]

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
    # TODO guardar a localizacao apenas quando o tempo da msg e superior ao anterior
    if float(info[4]) >= float(globaldict.dic_msg[sender][4]):
        globaldict.dic_msg[sender] = info

def cal_closer_semaphore(senderID , dist1):

    if globaldict.dic_msg[0][0] == 0:
        latDegrees = globaldict.dic_msg[0][1] * (-1)
    else:
        latDegrees = globaldict.dic_msg[0][1]
    if globaldict.dic_msg[0][2] == 0:
        lonDegrees = globaldict.dic_msg[0][3]* (-1)
    else:
        lonDegrees = globaldict.dic_msg[0][3]

    ambulance = (latDegrees, lonDegrees)
    print ambulance
    for key in globaldict.dic_msg:
        if key == senderID or key == 0:
            continue
        else:
            if globaldict.dic_msg[key][0] == 0:
                latDegrees2 = globaldict.dic_msg[key][1] * (-1)
            else:
                latDegrees2 = globaldict.dic_msg[key][1]
            if globaldict.dic_msg[key][2] == 0:
                lonDegrees2 = globaldict.dic_msg[key][3] * (-1)
            else:
                lonDegrees2 = globaldict.dic_msg[key][3]
            other_sem = (latDegrees2, lonDegrees2)

            dist2 = vincenty(ambulance, other_sem).miles
            print 'este e p semaforo' + str(key)
            print dist2
            print dist1

        if dist1 > dist2:  # Existe um semaforo mais proximo
            return False

    return True