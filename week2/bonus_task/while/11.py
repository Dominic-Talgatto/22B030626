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
c = arr[0]
for i in range(1, len(arr)):
    if c < arr[i]:
        m += 1
    c = arr[i]
print(m)
