deposit = float(input())
expiry = int(input())
percent = float(input())

lihva = (deposit * (percent / 100)) / 12
final_sum = deposit + lihva * expiry
print(final_sum)