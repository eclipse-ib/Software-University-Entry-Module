a1 = int(input())
a2 = int(input())
n = int(input())

s1 = " "
s2 = " "
s3 = " "

for first in range(a1, a2):
    s1 = chr(first)
    for second in range(1, n):
        s2 = second
        for third in range(1, (n // 2)):
            s3 = third
            s4 = ord(s1)
            if ord(s1) % 2 != 0 and (s2 + s3 + s4) % 2 != 0:
                print(f"{s1}-{s2}{s3}{s4}")
