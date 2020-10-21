n = int(input())

count = 0
number = 1

for i in range(1, n+1):
    for j in range(1, i+1):
        count += 1
        number += 1
        print(number)
