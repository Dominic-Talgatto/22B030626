n = int(input())
c = int(input())
a = 1

if n >= c:
    print(1)
else:
    while n < c:
        a += 1
        n = n * 1.1
    print(a)
