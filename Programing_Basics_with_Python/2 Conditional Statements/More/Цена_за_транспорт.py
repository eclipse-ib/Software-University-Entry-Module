km = int(input().lower())
time = input().lower()

if km < 20 and time == "day":
    taxi = km * 0.79 + 0.70
    print('%.2f' % taxi)

if km > 20 and km < 100 and time == "day":
    taxi = km * 0.79 + 0.70
    bus = km * 0.09
    if taxi < bus:
        print('%.2f' % taxi)
    else:
        print('%.2f' % bus)


if km > 100 and time == "day":
    taxi = km * 0.79 + 0.70
    bus = km * 0.09
    train = km * 0.06
    if taxi < bus:
        print('%.2f' % taxi)
    elif bus < train:
        print('%.2f' % bus)
    elif train < taxi:
        print('%.2f' % train)


if km < 20 and time == "night":
    taxi = km * 0.90 + 0.70
    print('%.2f' % taxi)

if km > 20 and km < 100 and time == "night":
    taxi = km * 0.90 + 0.70
    bus = km * 0.09
    if taxi < bus:
        print('%.2f' % taxi)
    else:
        print('%.2f' % bus)

if km > 100 and time == "night":
    taxi = km * 0.90 + 0.70
    bus = km * 0.09
    train = km * 0.06
    if taxi < bus:
        print('%.2f' % taxi)
    elif bus < train:
        print('%.2f' % bus)
    elif train < taxi:
        print('%.2f' % train)

