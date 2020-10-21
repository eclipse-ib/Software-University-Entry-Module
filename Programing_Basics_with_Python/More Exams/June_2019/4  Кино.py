capacity = int(input())

entered_people = 0
ticket_price = 5
all_money = 0

while True:
    people_in = input()
    if people_in == str("Movie time!"):
        print(f"There are {capacity} seats left in the cinema.")
        break
    if int(people_in) > capacity:
        print(f"The cinema is full.")
        break
    capacity = capacity - int(people_in)
    entered_people = entered_people + int(people_in)
    recived_money = int(people_in) * ticket_price
    if int(people_in) % 3 == 0:
        recived_money = (int(people_in) * ticket_price) - 5
    all_money = all_money + recived_money
print(f"Cinema income - {all_money} lv.")
