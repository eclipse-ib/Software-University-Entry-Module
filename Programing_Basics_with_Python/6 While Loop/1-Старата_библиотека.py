book_name = input()

count = 0

while True:
    next_book = input()
    if next_book.isdigit():
        continue
    elif next_book == "" or next_book == " ":
        continue
    elif next_book == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {count} books.")
        break
    else:
        count += 1