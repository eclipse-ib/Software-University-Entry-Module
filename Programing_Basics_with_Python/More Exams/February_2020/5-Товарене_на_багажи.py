# Вариант 1:

capacity = float(input())

size_of_suitcases = 0
count = 1

while True:
    current_suitcase_size = input().lower()
    if current_suitcase_size == "end".lower():
        print(f"Congratulations! All suitcases are loaded!")
        break
    if count % 3 == 0:
        current_suitcase_size = (float(current_suitcase_size) / 10) * 11
    size_of_suitcases = size_of_suitcases + float(current_suitcase_size)
    if capacity < size_of_suitcases:
        print(f"No more space!")
        break
    count += 1
print(f"Statistic: {count-1} suitcases loaded.")




# Вариант 2:

# capacity = float(input())
# count = 1
#
# while True:
#     current_suitcase_size = input().lower()
#     if current_suitcase_size == "end".lower():
#         print(f"Congratulations! All suitcases are loaded!")
#         break
#     if count % 3 == 0:
#         current_suitcase_size = (float(current_suitcase_size) / 10) * 11
#     capacity -= float(current_suitcase_size)
#     if capacity < 0:
#         print(f"No more space!")
#         break
#     count += 1
# print(f"Statistic: {count-1} suitcases loaded.")