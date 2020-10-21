count = 0
score = 0
name = " "
while True:
    count = count + 1
    if count > 7:
        print(f"The limit is reached.")
        break
    movie_name = input()
    if movie_name == "STOP":
        break
    name_lenght = len(movie_name)
    current_name = movie_name
    current_score = 0

    for i in movie_name:
        if ord(i) > 64 and ord(i) < 91:
            current_score = current_score + (ord(i) - len(movie_name))
        elif ord(i) > 96 and ord(i) < 123:
            current_score = current_score + (ord(i) - (2 * len(movie_name)))
        else:
            current_score = current_score + ord(i)

    if current_score > score:
        name = current_name
        score = current_score
print(f"The best movie for you is {name} with {score} ASCII sum.")