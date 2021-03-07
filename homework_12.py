##1
import requests
import json
import csv
import re


def get_quotes(number_of_quotes, create_file="homework_12_csv.csv"):
    quotes = set()
    while len(quotes) < number_of_quotes:
        url = "http://api.forismatic.com/api/1.0/"
        params = {"method": "getQuote",
                  "format": "json",
                  "key": 1,
                  "lang": "ru"}
        responce = requests.get(url, params=params)
        quote = responce.json()
        some_quotes = (quote["quoteAuthor"], quote["quoteText"], quote["quoteLink"])
        if quote["quoteAuthor"] != "":
            quotes.add(some_quotes)
    result = sorted(list(quotes), key=lambda quotes: quotes[1])
    with open(create_file, "w", newline="", encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(result)


get_quotes(6)

##2

##2.1

filename = "authors_12.txt"


def read_txt(filename):
    with open(filename, "r") as txt_file:
        data = []
        for line in txt_file.readlines():
            if line.find("'s") >= 0 and (line.find("birthday") >= 0 or line.find("death") >= 0):
                data.append(line)
    return data


authors = read_txt(filename)
# print(authors)


##2.2

def change_format(authors):
    new_file_format = []
    months = {
        'January': "01",
        'February': "02",
        'March': "03",
        'April': "04",
        'May': "05",
        'June': "06",
        'July': "07",
        'August': "08",
        'September': "09",
        'October': "10",
        'November': "11",
        'December': "12"
    }
    for text in authors:
        name = re.findall(r"[a-zA-Z. ]+[']", text)
        name = "".join(name)
        numbers = re.findall(r"[0-9]+", text)
        month = re.findall(r"[A-Z][a-z]+[ ][1]", text)
        month_name = "".join([i.strip(' 1') for i in month])
        dd = numbers[0] if len(numbers[0]) > 1 else "0" + numbers[0]
        mm = months[month_name]
        yyyy = numbers[1]
        date = f"{dd}/{mm}/{yyyy}"
        new_format = {"name": name, "date": date}
        new_file_format.append(new_format)
    return new_file_format


# result = change_format(authors)
# print(result)


##2.3
def add_authors_json(filename, authors):
    with open(filename, "w") as json_file:
        json.dump(change_format(authors), json_file, indent=2)


add_authors_json("homework_12_authors.json", authors)
