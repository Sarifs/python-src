import socket
import math

HOST = "challenge01.root-me.org"  # The server's hostname or IP address
PORT = 52018  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.sendall(b"Hello, world")
    data = s.recv(1024)
    print(data.decode()) # must be decoded to have the good view
    index = data.decode().find("please")
    print(data.decode()[index:])
    splited = data.decode()[index:].split(' ')
    print(splited)
    print(splited[1][:-3:]) # a
    print(splited[2]) # signe b
    print(splited[3][:-3:]) # b
    print(splited[4]) # signe c
    print(splited[5]) # c
    print(splited[7]) # - c

    a = int(splited[1][:-3:])
    b =  int(splited[3][:-3:]) * (-1) if splited[2] == '-' else int(splited[3][:-3:])
    c = int(splited[5]) * (-1) if splited[4] == '-' else int(splited[5])
    minus_c = int(splited[7][:-3:])
    c += -minus_c
    print("a = ",a,"b = ", b, "c =", c)
    
    delta = b * b - (4*a*c)
    print("delta = ",delta)

    if delta < 0:
        print("Not possible")
    elif  delta == 0:
        print(-b/(2 * a))
    else :
        x1 = round((-b - math.sqrt(delta))/(2 * a),3)
        x2 = round((-b + math.sqrt(delta))/(2 * a),3)
        print("x1 = ",x1,"x2 = ",x2)

    
    
