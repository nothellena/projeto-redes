import socket
from _thread import *
from utils import *
from ball import Ball
from player import Player

# COLORS AND CUSTOMIZATION
BG = 40, 42, 54
PINK = 255, 121, 198
GREEN = 80, 250, 123
CYAN = 139, 233, 253
WHITE = 255, 255, 255

ball = Ball(345, 255, GREEN, 10, 10)
size = 500
objects = [Player(100, ((size - 100) / 3 * 2) + 50, 10, 50, PINK, 'p'),
           Player(590, ((size - 100) / 3 * 2) + 50, 10, 50, CYAN, 'p'),
           Player(100, (size - 100) / 3, 10, 50, PINK, 'p'),
           Player(590, (size - 100) / 3, 10, 50, CYAN, 'p'),
           ball]


def thread(con, obj):
    con.send(str.encode(create_single_object_info(objects[obj])))
    rep = ""

    while True:
        try:
            x, y, data1, data2 = read_single_object_info(con.recv(2048).decode())

            # Atualiza posição do objeto
            objects[obj].x, objects[obj].y = x, y

            # Se o objeto for a bola, atualize os scores
            if objects[obj].type == 'b':
                objects[obj].scoreA, objects[obj].scoreB = data1, data2

            if not (x, y, data1, data2):
                print("Cliente desconectado")
                break
            else:

                # Filtra os dados dos outros objetos e os envia
                other_objects = [x for x in objects if x != objects[obj]]

                rep = create_objects_info(other_objects)

                print("Recebido:", (x, y, data1, data2))
                print("Enviando:", rep)

            con.sendall(str.encode(rep))

        except:
            break

    print("Conexão perdida.")
    con.close()


def main():
    current_obj = 0

    # SERVER CONFIGS

    server = "192.168.0.8"
    port = 5555

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((server, port))

    except socket.error as e:
        str(e)

    s.listen(5)

    print("Server ON! Aguardando conexões...")

    while True:
        con, end = s.accept()
        print("Conectado à:", end)

        start_new_thread(thread, (con, current_obj))
        current_obj += 1
