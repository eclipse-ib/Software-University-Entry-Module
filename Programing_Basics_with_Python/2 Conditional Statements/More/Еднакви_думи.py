# Моя начин:

word1 = input("Въведете първата дума: ")
word2 = input("Въведете втората дума: ")

if word1.lower() == word2.lower():
    print("Yes")
else:
    print("No")



# По СофтУни начина:

word1 = input("Въведете първата дума: ")
word2 = input("Въведете втората дума: ")

word1 = word1.lower()
word2 = word2.lower()

if word1 == word2:
    print("Yes")
else:
    print("No")