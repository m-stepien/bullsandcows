import socket
import threading
import RoomManager

class Serwer:
    HEADER = 128
    DISCONNECT = "!DISCONET"
    PORT = 5050

    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)




    def handle_client(self, conn, addr):
        connected = True
        while connected:
            msg_length = conn.recv(HEADER).decode('utf-8')
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode('utf-8')
                print(f"addr {addr} message {msg}")
                if msg == DISCONNECT:
                    connected = False
        conn.close()



    def start(self):
        server.listen()
        print(f"server listening on {SERVER}")
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"ACTIVE CONNECTION {threading.activeCount() - 1}")