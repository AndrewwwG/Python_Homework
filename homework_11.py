import json
import re

##1

filename = "11_json.json"


def read_json(filename):
    with open(filename, 'r', encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


data = read_json("11_json.json")


##2

# первый вариант (выводит фамилии, даты и текст)

def sort_by_surname(data):
    data["name"] = data["name"].split()[-1]
    return data["name"]


data = sorted(data, key=sort_by_surname)
for i in range(9):
    print(data[i])


# второй вариант (выводит только фамилии)

def sort_by_surname(data):
    return data["name"]


data = sorted(data, key=sort_by_surname)
for i in range(9):
    print(data[i]["name"].split()[-1])


##3

def sort_by_date(sort_years):
    my_year = sort_years["years"]
    year = re.findall(r'\d+', my_year)[-1]
    return -int(year) if "BC" in my_year[my_year.index(year):] else int(year)


data = sorted(data, key=sort_by_date)

for i in range(9):
    print(data[i]["years"])


##4

def sort_by_len_words(data):
    words = data["text"]
    words = words.split()
    len_words = len(words)
    return len_words


sort_data_by_words = sorted(data, key=sort_by_len_words)
print(sort_data_by_words)
