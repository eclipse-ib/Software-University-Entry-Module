n1 = int(input())
n2 = int(input())

for number in range(n1, n2+1):
    odd_sum = 0
    even_sum = 0
    count = 1
    for ech in str(number):
        if count % 2 == 0:
            even_sum += int(ech)
            count += 1
        else:
            odd_sum += int(ech)
            count += 1
    if odd_sum == even_sum:
        print(f"{number} ", end="")

