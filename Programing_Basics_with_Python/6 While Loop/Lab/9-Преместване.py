width = int(input())
length = int(input())
height = int(input())

all_free_space = width * length * height

while all_free_space > 0:
    num_boxes = input()
    if num_boxes == "Done":
        print(f"{all_free_space} Cubic meters left.")
        exit()
    all_free_space -= int(num_boxes)
print(f"No more free space! You need {abs(all_free_space)} Cubic meters more.")