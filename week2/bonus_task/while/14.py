a = 0
b = 1
c = 0
cnt = 0
m = int(input())
if m == 0:
    print(0)
elif m == 1:
    print(1)
else:
    for i in range(m - 1):
        c = b + a
        a = b
        b = c
    print(b)
