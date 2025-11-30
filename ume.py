import socket
import base64
import zlib


HOST = "challenge01.root-me.org"
PORT = 52022      

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while 1:
        data = s.recv(1024)
        print(data.decode())
        start = data.decode().find("'")
        end = data.decode().find(".")
        print(data.decode()[start + 1:end - 1])
        str = data.decode()[start + 1:end - 1]
        decoded = base64.b64decode(str.encode())
        print(f"decoded str = {decoded}")
        var = zlib.decompress(decoded)
        print(var)
        s.send(f"{var.decode()}\n".encode())
