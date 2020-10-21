n = int(input())

scores = n
count = 0

while not scores <= 0:
    sector = input().lower()
    if sector == "bullseye":
        count += 1
        print(f"Congratulations! You won the game with a bullseye in {count} moves!")
        exit()
    new_scores = int(input())
    if sector == "number section":
        scores = scores - new_scores
        count += 1
    elif sector == "double ring":
        scores = scores - (new_scores * 2)
        count += 1
    elif sector == "triple ring":
        scores = scores - (new_scores * 3)
        count += 1

if scores < 0:
    print(f"Sorry, you lost. Score difference: {abs(scores)}.")
else:
    print(f"Congratulations! You won the game in {count} moves!")


