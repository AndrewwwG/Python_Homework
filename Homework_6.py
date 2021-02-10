
##1

my_list = ['qwer', 'asdf', 'gvcxs', 'rdsrgf', 'rdewaih', 'yjhh', 'grfdeb', 'mkljuj', 'hgyrd']
new_list = []
for index, item in enumerate(my_list):
    if index % 2 !=0:
        new_list.append(item[::-1])
    else:
        new_list.append(item)
print(new_list)


######################################################################
######################################################################

##2

my_list = ['awer', 'asdf', 'gvcxs', 'adsrgf', 'adewaih', 'yjhh', 'arfdeb', 'mkljuj', 'hgyrd']
new_list = []
for item in my_list:
    if item[0] == 'a':
        new_list.append(item)
print(new_list)

######################################################################
######################################################################

##3

my_list = ['waer', 'asdf', 'gvcxs', 'dsragf', 'dewaih', 'yjahh', 'rfdeb', 'mkljuaj', 'hgyrd']
new_list = [items for items in my_list if 'a' in items]
print(new_list)


######################################################################
######################################################################

##4

my_list = ["qwe", 'asd', 'zxc', 'ert', 3, 5, '12']
str_list = [str(value) for value in my_list if type(value) == str]
print(str_list)


######################################################################
######################################################################or value.isdigit()

##5

my_str = 'wertyuihgfdscvjkiuytdsaxcmp'
my_result = []

for symbol in my_str:
    if my_str.count(symbol) == 1:
        my_result.append(symbol)

print(my_result)


######################################################################
######################################################################

##6

my_list_1 = 'asdfpqwqasdsfq'
my_list_2 = 'qwerpzx'
my_result = list(set(my_list_1) & set(my_list_2))
print(my_result)


######################################################################
######################################################################

##7

my_str_1 = "Qwjfhdcoijdsovijktbwsfjvszpl"
my_str_2 = "Fjdbndobjsvlsvsdjdvjsvpm"
set_my_str_1 = set(my_str_1)
set_my_str_2 = set(my_str_2)
result = []

for symbol in set_my_str_1.intersection(set_my_str_2):
    if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
        result.append(symbol)
print(result)


######################################################################
######################################################################

##8

person = {"Name": "John",
          "Surname": "McCain",
          "Age" : 72,
          "Address": { "Country": "USA",
                       "City": "Washington",
                       "Street": "1600 Pennsylvania Avenue"},
          "Place":   { "Ability": "Yes",
                       "Position": "Officer"}}
print(person["Address"])

######################################################################
######################################################################

##9

cake = { "Коржи":  {"Мука": "222gr",
                    "Молоко": "666ml",
                    "Масло": "155gr",
                    "Яйцо": "3"},
         "Крем":   {"Сахар": "155gr",
                    "Масло":  "333gr",
                    "Ваниль": "44gr",
                    "Сметана": "333gr"},
         "Глазурь": {"Какао": "555gr",
                    "Сахар": "333gr",
                    "Масло": "111gr"}}

print(cake["Крем"])




