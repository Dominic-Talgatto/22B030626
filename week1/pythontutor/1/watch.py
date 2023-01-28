a = int(input())
h = 0
if a <= 59:
    print(h, a)
else:
    while a >= 60:
        h += 1
        a -= 60
    while h >= 24:
        h -= 24
    print(h, a)
