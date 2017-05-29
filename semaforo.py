from geopy.distance import vincenty
import globaldict


def calcSentido(latEmisphere, latDegrees, lonEmisphere, lonDegrees, utc, semaphore, sender):
    if latEmisphere == 0:
        latDegrees = latDegrees * (-1)
    if lonEmisphere == 0:
        lonDegrees = lonDegrees * (-1)

    loc1 = (latDegrees, lonDegrees)
    loc_sem = (semaphore[0], semaphore[1])

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
