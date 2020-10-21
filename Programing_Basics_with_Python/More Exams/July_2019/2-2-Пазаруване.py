budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())

video_cards_price = 250
processors_price = (video_cards * video_cards_price) * 0.35
ram_memory_price = (video_cards * video_cards_price) * 0.10

final_price = (video_cards_price * video_cards) + (processors * processors_price) + (ram_memory * ram_memory_price)
if video_cards > processors:
    final_price = final_price * 0.85

diff = abs(budget - final_price)
if budget >= final_price:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")