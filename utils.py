def get_color(string):

    s = string.replace("(","").replace(")","")
    s = s.split(",")

    return (int(s[0]),int(s[1]),int(s[2]))

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
        return str(int(obj.x)) + "-" + str(int(obj.y)) + "-" + str(obj.scoreA) + "-" + str(obj.scoreB) + "-" + "(80, 250, 123)" + "-"+ "None"

    return str(int(obj.x)) + "-" + str(int(obj.y)) + "-" + str(int(obj.height)) + "-" + str(int(obj.width)) + "-" + str(obj.color) + "-" + str(obj.type)


def read_single_object_info(data):
    info_list = data.split("-")
    x, y = int(info_list[0]), int(info_list[1])
    height, width = int(info_list[2]), int(info_list[3])
    color = get_color(info_list[4])
    type = info_list[5]

    return x, y, height, width, color, type


def read_objects_info(data):
    objects_info = data.split(";")
    objects = []

    for obj in objects_info:
        x, y, height, width, color, type = read_single_object_info(obj)
        objects.append([x, y, height, width, color, type])

    return objects
