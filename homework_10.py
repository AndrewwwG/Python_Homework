import json
import csv


##1

def read_file_txt(filename):
    with open(filename, "r") as txt_file:
        data = txt_file.read()
    return data


def read_file_json(filename):
    with open(filename, "r") as json_file:
        data = json.load(json_file)
    return data


def read_file_csv(filename):
    with open(filename, "r", encoding="utf-8") as csv_file:
        data = []
        reader = csv.reader(csv_file)
        for row in reader:
            data.append(row)
    return data


def read_file(filename):
    extension = filename.rsplit(".", 1)[-1]
    if extension == 'txt':
        result = read_file_txt(filename)
    elif extension == 'json':
        result = read_file_json(filename)
    elif extension == 'csv':
        result = read_file_csv(filename)
    else:
        result = "Unsupported file format"
    return result


print(read_file('read_data_csv.csv'))


##2

def write_file_txt(filename, data):
    with open(filename, "w") as txt_file:
        data = txt_file.write(data)
    return data


def write_file_json(filename, data):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=2)
    return data


def write_file_csv(filename, data):
    with open(filename, 'w', encoding="utf-8") as csv_file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def write_file(filename, data):
    extension = filename.rsplit('.', 1)[-1]
    if extension == 'txt':
        write_file_txt(filename, data)
    elif extension == 'json':
        write_file_json(filename, data)
    elif extension == 'csv':
        write_file_csv(filename, data)
    else:
        "Unsupported file format"


data = [{'name': 'Pablo', 'age': 8},
        {'name': 'Anton', 'age': 92},
        {'name': 'Anna', 'age': 20},
        {'name': 'Anastasiia', 'age': 62}]

write_file('write_data_json.json', data)
