##1

my_list = [365, 421, 31, 114, 8]
for value in my_list:
    if value > 100:
        print(value)

########################################
########################################
##2

my_list = [450, 930, 510, 6, 7, 825, 9]
my_results = []
for numbers in my_list:
    if numbers > 100:
        my_results.append(numbers)
for numbers in my_results:
    print(numbers)


########################################
########################################
##3

my_list = [450, 825, 9]
if len(my_list) < 2:
    my_list.append(0)
elif len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])
print(my_list)


########################################
########################################
##5

my_list = [54, 10, 5, 88, 23, 142]
my_indexes = [0, 1, 2, 3, 4, 5]
for index in my_indexes:
    print(my_list[index])

##5 другой вариант получения результата

my_list = [54, 10, 5, 88, 23, 142]
my_indexes = [0, 1, 2, 3, 4, 5]
for index in my_indexes:
    print(f"{index} -> {my_list[index]}")


########################################
########################################
##6

my_indexes = [0, 1, 2, 3, 4, 5, 6]
my_list_1 = [5, 4, 2, 7, 3, 5, 8]
my_list_2 = [9, 6, 4, 6, 7, 8, 2]
my_list_3 = [(my_list_1[i], my_list_2[i]) for i in range(len(my_list_1))]
for index in range(len(my_list_3)):
    print(my_list_3[index])

##6 другой вариант получения результата

my_indexes = [0, 1, 2, 3, 4, 5, 6]
my_list_1 = [5, 4, 2, 7, 3, 5, 8]
my_list_2 = [9, 6, 4, 6, 7, 8, 2]
my_list_3 = [(my_list_1[i], my_list_2[i]) for i in range(len(my_list_1))]
for index in range(len(my_list_3)):
    print(f"{index} -> {my_list_3[index]}")

########################################
########################################
##7

my_string = '0123456789'
my_list = []
my_result = []
for symb_1 in my_string:
    for symb_2 in my_string:
        my_result = int(symb_1 + symb_2)
        my_list.append(my_result)
print(my_list)

