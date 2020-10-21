# first_name = input("First name: ")
# last_name = input("Last name: ")
# age = int(input("Age: "))
# city = input("City: ")
#
# print("You are " + first_name + " " + last_name + ", a " + str(age) + "-years old person from " + city + ".", end= '')


# --------------------------------

first_name = input("First name: ")
last_name = input("Last name: ")
age = int(input("Age: "))
city = input("City: ")

print("You are %s %s, a %d - years old person from %s "
% (first_name,last_name,age,city))