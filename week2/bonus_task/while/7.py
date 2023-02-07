a = 0
c = 1
while True:
    n = int(input())
    if n == 0:
        print(a / (c - 1))
        break
    a += n
    c += 1
