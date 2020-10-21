cake_width = int(input())
cake_height = int(input())

cake_size = cake_width * cake_height
taken = 0

while cake_size > 0:
    taken_pieces = input()
    if taken_pieces == "STOP":
        print(f"{cake_size} pieces are left.")
        exit()
    taken += int(taken_pieces)
    cake_size -= int(taken_pieces)
print(f"No more cake left! You need {abs(cake_size)} pieces more.")