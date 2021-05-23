import socket
from _thread import *
from player import Player
import pickle

def thread(con,player):
    con.send(pickle.dumps(players[player]))
    rep = ""

    while True:
        try:
            data = pickle.loads(con.recv(2048))
            players[player] = data

            if not data:
                print("Cliente desconectado")
                break
            else:
                rep = [x for x in players if x != players[player]]

                print("Recebido:",rep)
                print("Enviando:", rep)

            con.sendall(pickle.dumps(rep))

        except:
            break

    print("Conexão perdida.")
    con.close()

#COLORS AND CUSTOMIZATION
PINK = 255, 121, 198
GREEN = 80, 250, 123
CYAN = 139, 233, 253
YELLOW = 241, 250, 140
RED = 255, 85, 85

size = 300

players = [Player(size/2 - 50, 0, 100, 10, PINK, 'h'), Player(size/2 - 50, size-10, 100, 10, CYAN, 'h'),
           Player(0, size/2 - 50, 10, 100, YELLOW, 'v'), Player(size-10, size/2 - 50, 10, 100, RED, 'v')]

current_player = 0

#SERVER CONFIGS

server = "192.168.0.8"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))

except socket.error as e:
    str(e)

s.listen(4)

print("Server ON! Aguardando conexões...")

while True:
    con, end = s.accept()
    print("Conectado à:",end)

    start_new_thread(thread,(con,current_player))
    current_player+=1

