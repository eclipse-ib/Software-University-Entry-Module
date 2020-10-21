# sum = float(input())
# val_1 = input()
# val_2 = input()
#
#
#
# lev = 1.00
# usd = lev * 1.79549
# eur = lev * 1.95583
# gbr = lev * 2.53405
#
# conv = val_1 * sum * val_2
#
# print(conv)

money = float(input())
currency_1 = input()
currency_2 = input()
this_dict = dict(BGN=1, USD=1.79549, EUR=1.95583, GBP=2.53405)
result = money * (this_dict[currency_1] / this_dict[currency_2])
print(f'{result:.2f} {currency_2}')





currency = {'BGN': 1, 'USD': 1.79549, 'EUR': 1.95583, 'GBP': 2.53405}

money = float(input())
currency_in = input()
currency_out = input()

result = currency[currency_in] / currency[currency_out]*money
print(f'{result:.2f}')






sum = float(input())
type_currency_in = input()
type_currency_out = input()

BGN_ = 1
USD_ = 1.79549
EUR_ = 1.95583
GBP_ = 2.53405

if type_currency_in == "BGN":
    sum = sum * BGN_
elif type_currency_in == "USD":
    sum = sum * USD_
elif type_currency_in == "EUR":
    sum = sum * EUR_
elif type_currency_in == "GBP":
    sum = sum * GBP_

if type_currency_out == "USD":
    result = sum / USD_
elif type_currency_out == "EUR":
    result = sum / EUR_
elif type_currency_out == "GBP":
    result = sum / GBP_
elif type_currency_out == "BGN":
    result = sum / BGN_

print(f"{result:.2f}")
