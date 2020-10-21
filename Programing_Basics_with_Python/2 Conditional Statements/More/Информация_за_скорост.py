speed = float(input())

if speed <= 10:
    print("The speed is too slow")
elif speed > 10 and speed <= 50:
    print("The speed is average")
elif speed > 50 and speed <= 150:
    print("The speed is fast")
elif speed > 150 and speed <= 1000:
    print("The speed is ultra fast")
else:
    print("The speed is extremely fast")