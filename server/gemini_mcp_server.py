import socket

HOST = "127.0.0.1"
PORT = 5555

def send_to_blender(code: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(code.encode("utf-8"))
    s.close()
