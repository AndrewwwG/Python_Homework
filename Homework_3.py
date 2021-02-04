
##1

value = input("Enter a number:")
if value.isdigit():
    new_value = int(value)
    if new_value < 100:
        print(new_value / 2)
    elif new_value > 100:
        print(new_value * -1)


##1 другой вариант записи


value = input("Enter a number:")
if value.isdigit():
    new_value = int(value)
    result = new_value / 2 if new_value < 100 else new_value *-1
    print(result)

##############################################
##############################################

##2

value = input("Enter a number:")
if value.isdigit():
    new_value = int(value)
    if new_value < 100:
        result = 1
    elif new_value > 100:
        result = 0
    print(result)


##2 другой вариант записи


value = input("Enter a number:")
if value.isdigit():
    new_value = int(value)
    result = 1 if new_value < 100 else 0
    print(result)


##############################################
##############################################


##3


value = input("Enter a number:")
if value.isdigit():
    new_value = int(value)
    result = True if new_value < 100 else False
    print(result)


##3 другой вариант записи


value = input("Enter a number:")
if value.isdigit():
    new_value = int(value)
    if new_value < 100:
        print(True)
    elif new_value > 100:
        print(False)


##############################################
##############################################

##4

my_str = "QWERT testiNg strIng 123"
my_str = my_str.upper()
print(my_str)


##############################################
##############################################
##############################################

##5

my_str = "QWERT tesTing sTriNg 123"
my_str = my_str.lower()
print(my_str)


##############################################
##############################################

##6

value = input("Enter the string:")
my_str = str(value)
if len(my_str) < 5:
    print(my_str*2)
elif len(my_str) > 5:
    print(my_str)


##############################################
##############################################

##7

value = input("Enter the string:")
my_str = str(value)
if len(my_str) < 5:
    print(value+my_str[::-1])
elif len(my_str) > 5:
    print(my_str)


##############################################
##############################################

##8

my_str = "123/Ukraine.com"
for symbol in my_str:
    if symbol.isalnum():
        print(f"symbol:{symbol}'")


##############################################
##############################################

##9

my_str = "1-2?3_Ukraine.com ua ua 1."
for symbol in my_str:
    if not symbol.isalnum():
        print(f"symbol:{symbol}'")


###############################################
###############################################

##10

my_str = "1-2 ?3_Ukraine is Ukraine  -       com/"
for symbol in my_str:
    if not symbol.isalnum() and symbol !=" ":
        print(f"symbol:{symbol}'")

