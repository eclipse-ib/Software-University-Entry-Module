people = int(input())

all_cookies = 0
all_cakes = 0
all_waffles = 0
cookies = 0
cakes = 0
waffles = 0
for i in range(people):

    name = input()
    sugar_thing = input().lower()
    while not sugar_thing == "stop baking!":
        number = int(input())
        if sugar_thing == "cookies":
            cookies = cookies + number

        elif sugar_thing == "cakes":
            cakes = cakes + number

        elif sugar_thing == "waffles":
            waffles = waffles + number

        sugar_thing = input().lower()
    print(f"{name} baked {cookies} cookies, {cakes} cakes and {waffles} waffles.")
    all_cookies = all_cookies + cookies
    all_cakes = all_cakes + cakes
    all_waffles = all_waffles + waffles
    cookies = 0
    cakes = 0
    waffles = 0
all_sugar_things = all_cookies + all_cakes + all_waffles
print(f"All bakery sold: {all_sugar_things}")

one_cookie_price = 1.50
one_cake_price = 7.80
one_waffle_price = 2.30

total_sum = (all_cookies * one_cookie_price) + (all_cakes * one_cake_price) + (all_waffles * one_waffle_price)
print(f"Total sum for charity: {total_sum:.2f} lv.")
