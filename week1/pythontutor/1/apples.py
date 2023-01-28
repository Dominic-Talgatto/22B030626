a = int(input())
b = int(input())

if b % a == 0:
    print(int(b / a))
    print(0)
else:
    print(b // a)
    print(b - a * (b // a))
