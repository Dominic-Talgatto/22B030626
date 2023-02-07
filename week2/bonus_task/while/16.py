arr = []

max = 0
cnt = 0

while True:
    n = int(input())
    if n != 0:
        arr.append(n)
    else:
        break

a = arr[0]

for i in range(1, len(arr)):
    if a == arr[i]:
        cnt += 1
    else:
        a = arr[i]
        cnt = 0
    if cnt > max:
        max = cnt
print(max + 1)
