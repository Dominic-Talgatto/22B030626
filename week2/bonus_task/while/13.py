a = 1
c = 0
m = 0
arr = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        arr.append(n)
arr.sort()
for i in arr:
    if i == arr[-1]:
        c += 1
print(c)
