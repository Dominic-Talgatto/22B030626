a = 0
c = 0
m = 0
while True:
    n = int(input())
    if n == 0:
        print(m)
        break
    c += 1
    if n > a:
        a = n
        m = c
