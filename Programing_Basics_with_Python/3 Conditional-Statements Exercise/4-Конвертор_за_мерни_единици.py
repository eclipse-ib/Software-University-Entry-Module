number = float(input())
in_unit = input()
out_unit = input()

exit_unit = 0

if in_unit == "m" and out_unit == "cm":
    exit_unit = number * 100
elif in_unit == "m" and out_unit == "mm":
    exit_unit = number * 1000
elif in_unit == "m" and out_unit == "m":
    exit_unit = number
elif in_unit == "cm" and out_unit == "cm":
    exit_unit = number
elif in_unit == "cm" and out_unit == "mm":
    exit_unit = number * 10
elif in_unit == "cm" and out_unit == "m":
    exit_unit = number / 100
elif in_unit == "mm" and out_unit == "cm":
    exit_unit = number / 10
elif in_unit == "mm" and out_unit == "mm":
    exit_unit = number
elif in_unit == "mm" and out_unit == "m":
    exit_unit = number / 1000
print(f"{exit_unit:.3f}")
