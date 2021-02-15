
##1

from random import randint

import random
names = ["king", "ivan", "assasin", "harry"]
random_number = random.randint(100, 1000)
random_word = ''.join(chr(randint(ord('a'), ord('z'))) for j in range(randint(5, 7)))
domains = ["com", "ua", "de", "uk", "es"]
e_mail = random.choice(names) + "." + str(random_number) + "@" + str(random_word) + "." + random.choice(domains)
print(e_mail)


##2


import string
import random
min_len = 100
max_len = 110
digits = string.digits
def create_random_str(min_len, max_len):
    my_string = string.ascii_lowercase
    count = random.randint(min_len, max_len)
    return my_string * count


##3



def create_space(rand_str):
    index = 0
    rand_str_to_list = list(rand_str)
    condition = True
    while condition:
        step = random.randint(1, 10)
        index += step
        if index < len(rand_str):
            rand_str_to_list[index] = " "
        else:
            condition = False
    rand_str = "".join(rand_str_to_list)

    return rand_str

def modify_word(word, elements_upd=0.3):
    if random.random() < elements_upd:
        word = word.capitalize()
    if random.random() < elements_upd:
        word += ","
    if random.random() < elements_upd:
        word += '. \n'
    return word

def add_digits(word, elements_upd = 0.5):
    if random.randint(3, 100) < elements_upd:
        my_word = list(word)
        my_word.clear()
        for symbol in range(len(word)):
            my_word.append(str(random.randint(3, 100)))
        word = ' '.join(my_word)
    return word

def modify_str(rand_str):
    rand_str_split = rand_str.split()
    result = []
    rand_str_split[0] = rand_str_split[0].capitalize()
    for word in rand_str_split:
        word = modify_word(word)
        word = add_digits(word)
        result.append(word)
    return " ".join(result)


rand_str = create_random_str(0, 100)
rand_str = create_space(rand_str)
rand_str = modify_str(rand_str)
rand_str = add_digits(rand_str)
print(rand_str)






