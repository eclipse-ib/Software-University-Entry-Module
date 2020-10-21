n = int(input())

odd_sum = 0.00
odd_min = 9223372036854775807
odd_max = -9223372036854775807
even_sum = 0.00
even_min = 9223372036854775807
even_max = -9223372036854775807

for i in range(1, n+1):
    number = float(input())
    if i % 2 == 0:
        even_sum = even_sum + number
        if number > even_max:
            even_max = number
        if number < even_min:
            even_min = number
    else:
        odd_sum = odd_sum + number
        if number > odd_max:
            odd_max = number
        if number < odd_min:
            odd_min = number

print(f"OddSum={odd_sum:.2f},")
if odd_min == 9223372036854775807:
    print(f"OddMin=No,")
else:
    print(f"OddMin={odd_min:.2f},")
if odd_max == -9223372036854775807:
    print(f"OddMax=No,")
else:
    print(f"OddMax={odd_max:.2f},")
print(f"EvenSum={even_sum:.2f},")
if even_min == 9223372036854775807:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={even_min:.2f},")
if even_max == -9223372036854775807:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={even_max:.2f}")

