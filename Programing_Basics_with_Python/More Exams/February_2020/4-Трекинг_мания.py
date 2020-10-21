groups = int(input())

musala = 0
monblan = 0
kili = 0
k2 = 0
everest = 0

for i in range(groups):
    number = int(input())
    if number <= 5:
        musala = musala + number
    elif number > 5 and number <= 12:
        monblan = monblan + number
    elif number > 12 and number <= 25:
        kili = kili + number
    elif number > 25 and number <= 40:
        k2 = k2 + number
    elif number > 40:
        everest = everest + number

all_people = musala + monblan + kili + k2 + everest

percent_1 = (musala / all_people) * 100
percent_2 = (monblan / all_people) * 100
percent_3 = (kili / all_people) * 100
percent_4 = (k2 / all_people) * 100
percent_5 = (everest / all_people) * 100

print(f"{percent_1:.2f}%")
print(f"{percent_2:.2f}%")
print(f"{percent_3:.2f}%")
print(f"{percent_4:.2f}%")
print(f"{percent_5:.2f}%")