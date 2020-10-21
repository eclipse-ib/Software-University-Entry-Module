import math
tmpw = " "
value = 0
is_first_vowel = " "
while True:
    current_value = 0
    word = input()
    if word == "End of words":
        break

    for i in word:
        current_value = current_value + ord(i)

    for first in word:
        if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u' or first == 'y':
            is_first_vowel = True
            current_value = current_value * len(word)
        elif first == 'A' or first == 'E' or first == 'I' or first == 'O' or first == 'U' or first == 'Y':
            current_value = current_value * len(word)
        else:
            is_first_vowel = False
            current_value = current_value / len(word)
        if current_value > value:
            value = math.floor(current_value)
            tmpw = word
        break
print(f"The most powerful word is {tmpw} - {value}")
