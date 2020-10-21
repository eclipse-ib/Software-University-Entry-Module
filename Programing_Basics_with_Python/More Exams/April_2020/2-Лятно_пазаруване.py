budget = int(input())
towel_price = float(input())
discount = int(input())

umbrella_price = towel_price / 3 * 2
flip_flops_price = umbrella_price / 4 * 3
beach_bag_price = (towel_price + flip_flops_price) / 3

disc = discount / 100
final_price = (towel_price + umbrella_price + flip_flops_price + beach_bag_price)
final_price_w_d = final_price - (final_price * disc)
diff = abs(budget - final_price_w_d)

if budget >= final_price_w_d:
    print(f"Annie's sum is {final_price_w_d:.2f} lv. She has {diff:.2f} lv. left.")
else:
    print(f"Annie's sum is {final_price_w_d:.2f} lv. She needs {diff:.2f} lv. more.")
