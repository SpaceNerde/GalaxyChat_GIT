import socket
import threading as Thread

HOST = "0.0.0.0"
PORT = "97822"
seperator_token = "<SEP>"

client_sockets = set()

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)
print(f"[*] Listening as {HOST}:{PORT}")

def listen_for_client(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()

        except Exception as e:
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)

        else:
            msg = msg.replace(seperator_token, ": ")

        for client_socket in client_sockets:
            client_socket.send(msg.encode())

while True:
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.")
    client_sockets.add(client_socket)
    t = Thread(target=listen_for_client, args=(client_socket,))
    t.daemon = True
    t.start()

for cs in client_socket:
    cs.close()

s.close()