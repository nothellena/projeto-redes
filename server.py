import socket
from _thread import *
from utils import *
from ball import Ball
from player import Player

def thread(con,player):
    con.send(str.encode(create_single_object_info(players[player])))
    rep = ""

    while True:
        try:
            x, y, height, width, color, type = read_single_object_info(con.recv(2048).decode())
            players[player].x, players[player].y = x,y

            if players[player].type == 'b':
                players[player].scoreA, players[player].scoreB = height, width

            if not (x,y):
                print("Cliente desconectado")
                break
            else:

                objects = [x for x in players if x != players[player]]

                rep = create_objects_info(objects)

                print("Recebido:",(x, y, height, width, color, type))
                print("Enviando:", rep)

            con.sendall(str.encode(rep))

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


size = 400

ball = Ball(90,120,GREEN,10,10)

players = [Player(100, ((size - 100)/3 * 2) + 50, 10, 50, PINK, 'p'), Player(600, ((size - 100)/3 * 2) + 50, 10, 50, CYAN, 'p'),
           Player(100, (size - 100)/3, 10, 50, PINK, 'p'), Player(600, (size - 100)/3, 10, 50, CYAN, 'p'),ball]


current_player = 0

#SERVER CONFIGS

server = "192.168.0.8"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))

except socket.error as e:
    str(e)

s.listen(5)

print("Server ON! Aguardando conexões...")

while True:

    con, end = s.accept()
    print("Conectado à:",end)

    start_new_thread(thread,(con,current_player))
    current_player+=1

