import socket
import threading
import IdGenerator
HEADER_START = 64
DISCONNECT = "!DISCONET"
PORT = 5050

SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

id_gen = IdGenerator.IdGenerator()
def create_game_room(conn, addr):
    id = id_gen.give_me_id(addr)
    not_paired = True
    while connected and not_paired:
        msg_length = conn.recv(HEADER_START).decode('utf-8')
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode('utf-8')
            print(f"addr {addr} message {msg}")
            if msg == DISCONNECT:
                connected = False
    conn.close()


def start():
    server.listen()
    print(f"server listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"ACTIVE CONNECTION {threading.activeCount() - 1}")


print("STARTING SERVER")
start()
