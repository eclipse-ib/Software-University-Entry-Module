number_of_bitcoins = int(input())
number_of_china_val = float(input())
comis = float(input())

one_bitcoin = 1168
one_dollar = 1.76
one_chin_val = 0.15 * one_dollar
one_euro = 1.95

bitcoins_in_leva = number_of_bitcoins * one_bitcoin
china_val_in_leva = number_of_china_val * one_chin_val

sum_in_euro = (bitcoins_in_leva + china_val_in_leva) / 1.95
sum_in_euro_with_comis = sum_in_euro - ((comis/100)*sum_in_euro)
print(f"{sum_in_euro_with_comis:.2f}")
