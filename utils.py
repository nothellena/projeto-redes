def get_color(string):
    s = string.replace("(", "").replace(")", "")
    s = s.split(",")

    return (int(s[0]), int(s[1]), int(s[2]))

#Une as strings referentes a cada objeto em uma única string
def create_objects_info(objects):
    i = 0
    data = ""

    while True:
        i += 1
        data += create_single_object_info(objects[i - 1])

        if i == len(objects):
            return data

        data += ";"

# Cria string com os dados dos objetos
def create_single_object_info(obj):
    # Cada string contém 4 informações
    # Caso o objeto seja a bola, a string irá conter sua posição (x,y) e a pontuação de cada dupla
    if obj.type == 'b':
        return str(int(obj.x)) + "-" + str(int(obj.y)) + "-" + str(obj.scoreA) + "-" + str(obj.scoreB)

    # Caso seja um jogador, a string contem sua posição, sua cor e um indicador de que o objeto é um jogador("p")
    return str(int(obj.x)) + "-" + str(int(obj.y)) + "-" + str(obj.color) + "-" + "p"


# Extrai os dados da string

def read_single_object_info(data):
    info_list = data.split("-")
    x, y = int(info_list[0]), int(info_list[1])
    last = info_list[3]

    if last == 'p':
        data1 = get_color(info_list[2])
        data2 = last
    else:
        data1 = int(info_list[2])
        data2 = int(last)

    return x, y, data1, data2

# Particiona a string completa em substrings, cada uma referente a um objeto
def read_objects_info(data):
    objects_info = data.split(";")
    objects = []

    for obj in objects_info:
        x, y, data1, data2 = read_single_object_info(obj)
        objects.append([x, y, data1, data2])

    return objects
