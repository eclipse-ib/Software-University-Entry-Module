n1 = int(input())
n2 = int(input())
operator = input()

result = 0
is_even = "even"

if operator == "+":
    result = n1 + n2
    if result % 2 == 0:
        is_even = "even"
    else:
        is_even = "odd"
elif operator == "-":
    result = n1 - n2
    if result % 2 == 0:
        is_even = "even"
    else:
        is_even = "odd"
elif operator == "*":
    result = n1 * n2
    if result % 2 == 0:
        is_even = "even"
    else:
        is_even = "odd"
elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
        exit()
    else:
        result = n1 / n2
        print(f"{n1} / {n2} = {result:.2f}")
elif operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
        exit()
    else:
        result = n1 % n2
        print(f"{n1} % {n2} = {result}")
if operator == "+" or operator == "-" or operator == "*":
    print(f"{n1} {operator} {n2} = {result} - {is_even}")
