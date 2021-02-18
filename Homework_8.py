import random as randint
import string
min = 100
max = 1000


##1

names = ["king", "ivan", "assasin", "harry"]
domains = ["com", "ua", "de", "uk", "es"]
len_of_str = randint.randint(5, 7)

def create_str():
    str_letters = string.ascii_lowercase
    random_str = ''.join(randint.choice(str_letters) for i in range(len_of_str))
    return random_str

def create_email(names,domains):
    my_email = f'{names[randint.randint(0, len(names))]}.{randint.randint(min, max)}@'\
     f'{create_str()}.{domains[randint.randint(0, len(domains))]}'
    return my_email

e_mail = create_email(names, domains)
print(e_mail)


##2


def create_random_str(min_1, max_2):
    my_string = string.ascii_lowercase
    count = randint.randint(min_1, max_2)
    random_str = "".join(randint.choice(my_string) for i in range(count))
    return random_str
new_str = create_random_str(0, 100)



##3

def create_space(rand_str):
    index = 0
    rand_str_to_list = list(rand_str)
    while True:
        step = randint.randint(1, 10)
        index += step
        if index < len(rand_str):
            rand_str_to_list[index] = " "
        else:
            break
    rand_str = "".join(rand_str_to_list)

    return rand_str

def modify_word(word, elements_upd=0.5):
    if randint.random() < elements_upd:
        word = word.capitalize()
    if randint.random() < elements_upd:
        word += ","
    if randint.random() < elements_upd:
        word += '.\n'
    return word

def add_digits(word, elements_upd = 10):
    if randint.randint(1, 70) < elements_upd:
        my_word = list(word)
        my_word.clear()
        for symbol in range(len(word)):
            my_word.append(str(randint.randint(1, 70)))
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







