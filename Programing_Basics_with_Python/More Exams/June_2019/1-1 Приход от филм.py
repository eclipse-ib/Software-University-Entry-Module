name = input()
days = int(input())
tickets = int(input())
price = float(input())
cinema_percent = int(input())

profit = (days * tickets) * price
cinema_percent = cinema_percent / 100
final_sum = profit - (profit * cinema_percent)
print(f"The profit from the movie {name} is {final_sum:.2f} lv.")