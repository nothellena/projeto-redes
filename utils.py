def get_color(string):
    s = string.replace("(", "").replace(")", "")
    s = s.split(",")

    return (int(s[0]), int(s[1]), int(s[2]))


def create_objects_info(objects):
    i = 0
    data = ""

    while True:
        i += 1
        data += create_single_object_info(objects[i - 1])

        if i == len(objects):
            return data

        data += ";"


def create_single_object_info(obj):
    if obj.type == 'b':
        return str(int(obj.x)) + "-" + str(int(obj.y)) + "-" + str(obj.scoreA) + "-" + str(obj.scoreB)

    return str(int(obj.x)) + "-" + str(int(obj.y)) + "-" + str(obj.color) + "-" + "p"


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


def read_objects_info(data):
    objects_info = data.split(";")
    objects = []

    for obj in objects_info:
        x, y, data1, data2 = read_single_object_info(obj)
        objects.append([x, y, data1, data2])

    return objects
