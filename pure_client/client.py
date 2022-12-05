import socket

HEADER = 64
PORT = 5050
DISCONECT = "!DISCONET"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    mmessage = msg.encode('utf-8')
    msg_length = len(mmessage)
    send_length = str(msg_length).encode('utf-8')
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(mmessage)


send("Hello world!")
send("Gello")
send("Kupa")
send(DISCONECT)