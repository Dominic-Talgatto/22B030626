n = int(input())
c = 0
a = 0
while True:
    if 2 ** c > n:
        print(c - 1, 2 ** (c-1))
        break
    elif 2 ** c == n:
        print(c, 2 ** c)
        break
    c += 1
