
##1

value = "17206035138486283571265300000"
count = value.count("0")
print(count)


#########################################
#########################################

##2

value = "580587000"
print(len(value) - len(value.rstrip('0')))


#########################################
#########################################

##3a

my_list_1 = [2, 23, 11, 22, 34, 5, 8]
my_list_2 = [5, 66, 6, 2, 38, 87, 78]
my_result = []
for index, symbol in enumerate(my_list_1):
    if index % 2:
        my_result.append(symbol)
for symbol in my_list_2[::2]:
    my_result.append(symbol)
print(my_result)


#########################################
#########################################

##3b

my_list_1 = [14, 2, 33, 41, 57, 55, 68]
my_list_2 = [10, 13, 44, 12, 18, 15, 20, 25]
my_result = []
my_result = [numbers for numbers in my_list_1 if not numbers % 2] + [numbers for numbers in my_list_2 if numbers % 2]
print(my_result)


#########################################
#########################################

##4

my_list = [3, 56, 33, 587, 432]
new_list = []
new_list = my_list[1:] + [my_list[0]]
print(new_list)


#########################################
#########################################

##5

my_list = [1, 2, 3, 4]
my_list = my_list[1:] + [my_list.pop(0)]
print(my_list)


#########################################
#########################################

##6

import re
my_str = "43 больше чем 34 но меньше чем 56"
sum_of_numbers = sum(map(int, re.findall('(\d+)', my_str)))
print(sum_of_numbers)


#########################################
#########################################

##7

import re
my_str ='abcde'
my_str += '_' * (len(my_str) % 2)
print(re.findall('.{%s}' % 2, my_str))


#########################################
#########################################

##8

my_str = 'My_long str'
l_limit = 'o'
r_limit = 't'
index_l_limit = my_str.index(l_limit)
index_r_limit = my_str.index(r_limit)
print(my_str[index_l_limit + 1:index_r_limit])


#########################################
#########################################

##9

my_str = 'My_long string'
l_limit = 'o'
r_limit = 'g'
index_l_limit = my_str.index(l_limit)
index_r_limit = my_str.rindex(r_limit)
print(my_str[index_l_limit + 1:index_r_limit])


#########################################
#########################################

##10

my_list = [2, 8, 12, 7, 3, 9, 0, 34]
print(sum([my_list[i-1] < my_list[i] > my_list[i+1] for i in range(1, len(my_list)-1)]))
