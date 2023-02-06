a = int(input())
b = int(input())
arr = []

for i in range(b, a + 1):
    if i % 2 == 1:
        arr.append(i)
arr.reverse()
for i in arr:
    print(i, end=" ")
