##1

import random

n = 20
my_random = [random.randint(1, 100) for i in range(n)]
print(my_random)


##2

import random as rnd

def create_random_point():
    point = (rnd.randint(-10, 10),
             rnd.randint(-10, 10),
             rnd.randint(-10, 10))
    return point

def print_point(point):
    for key, value in point.items():
        print(f"Name: {key}, point: {value}")
triangle =  {'A': create_random_point(),
             'B': create_random_point(),
             'C': create_random_point()}
print_point(triangle)


##3

def my_print(string):
    string = '***' + string + '***'
    return string
my_str = "my_string"
print(my_print(my_str))


##4

from collections import defaultdict

persons = [{"name": "Ivan", "age": 68},
           {"name": "Anatolii", "age": 32},
           {"name": "Tatiana", "age": 22},
           {"name": "Andrii", "age": 12},
           {"name": "John", "age": 40}]

age_by_names = defaultdict(list)
len_name_by_names = defaultdict(list)
ages = []

for person in persons:
    name = person['name']
    age = person['age']
    age_by_names[age].append(name)
    len_name_by_names[len(name)].append(name)
    ages.append(age)

min_age = min(age_by_names)
print('Min_age:', *age_by_names[min_age])

max_len_name = max(len_name_by_names)
print('Max_len_name:', *len_name_by_names[max_len_name])
print('Average age:', sum(ages) // len(ages))


##5

dict_one = {11: 'red',
            2: 'green',
            32: 'blue',
            4: 'yellow',
            5: 'grey',
            6: 'orange',
            7: 'pink', }

dict_two = {1: 'blue',
            2: 'red',
            3: 'green',
            44: 'orange',
            5: 'grey',
            65: 'yellow',
            7: 'pink', }

##5.1

my_list = []

set_dict_one = set(dict_one)
set_dict_two = set(dict_two)
for key in set_dict_one.intersection(set_dict_two):
    my_list.append(key)
print(my_list)


##5.2

my_list_2 = []

for key in set_dict_one:
    if list(set_dict_two).count(key) == 0:
        my_list_2.append(key)
print(my_list_2)


##5.3

new_dict = {}

for key, value in dict_one.items():
    if list(dict_two).count(key) == 0:
        new_dict[key] = value
print(new_dict)


##5.4

new_dict_1 = {}

for key, value in dict_one.items():
    if list(dict_two).count(key) == 0:
        new_dict_1[key] = value

for key, value in dict_two.items():
    if list(dict_one).count(key) == 0:
        new_dict_1[key] = value

for key in set_dict_one.intersection(set_dict_two):
    new_dict_1[key] = dict_one[key], dict_two[key]

print(new_dict_1)



