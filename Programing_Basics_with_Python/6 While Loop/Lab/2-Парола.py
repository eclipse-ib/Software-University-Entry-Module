# user = input()
# password = input()
#
# while True:
#     repass = input()
#     if repass == password:
#         print(f"Welcome {user}!")
#         break

# Вариант 2:
user = input()
password = input()

repass = password

while repass != password:
    repass = input()
print(f"Welcome {user}!")