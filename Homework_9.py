import json
import random as rnd
import string

##1

path = "names.txt"
surnames = []
with open(path, "r") as txt_file:
    data = []
    for line in txt_file.readlines():
        data.append(line.strip())
    for names in data:
        names = names.split('\t')
        surnames.append(names[1])

print(surnames)

##2

my_result = []
rnd_dict = {}


def create_random_str():
    my_string = string.ascii_lowercase
    random_str = "".join(rnd.choice(my_string) for i in range(5))
    return random_str


def create_values():
    my_values = [int, float, bool]
    value_result = rnd.choice(my_values)
    if value_result == int:
        value_result = int(rnd.randint(-100, 100))
    if value_result == float:
        value_result = float(rnd.random())
    if value_result == bool:
        value_result = bool(rnd.randint(0, 1))
    return value_result


def create_rnd_dict():
    for i in range(rnd.randint(5, 20)):
        rnd_dict[create_random_str()] = create_values()
    return rnd_dict


print(create_rnd_dict())

##3

filename = "json.json"


def generate_and_write_json(filename):
    with open(filename, "w") as json_file:
        data = create_rnd_dict()
        json.dump(data, json_file, indent=2)


generate_and_write_json(filename)
