import socket
import threading

HOST = "0.0.0.0"
PORT = "97822"
seperator_token = "<SEP>"

client_sockets = set()

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)
print(f"[*] Listening as {HOST}:{PORT}")
