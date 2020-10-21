remain = float(input())

remain = remain * 100
count = 0

while remain > 0:
    if remain >= 200:
        remain -= 200
        count += 1
    elif remain >= 100:
        remain -= 100
        count += 1
    elif remain >= 50:
        remain -= 50
        count += 1
    elif remain >= 20:
        remain -= 20
        count += 1
    elif remain >= 10:
        remain -= 10
        count += 1
    elif remain >= 5:
        remain -= 5
        count += 1
    elif remain >= 2:
        remain -= 2
        count += 1
    elif remain >= 1:
        remain -= 1
        count += 1
print(count)