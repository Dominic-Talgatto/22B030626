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
print(arr[-2])
