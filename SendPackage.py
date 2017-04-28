def sendpackage(pacote):
    # recebe o pacote e envia o pacote para a rede wifi
    import socket
    HOST = '192.168.0.106'
    PORT = 5002
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    conn.send(pacote)

    return 0
