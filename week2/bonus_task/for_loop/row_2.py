a = int(input())
b = int(input())
arr = []

if b >= a:
    for i in range(a, b + 1):
        print(i, end=" ")
else:
    for i in range(b, a + 1):
        arr.append(i)
    arr.reverse()
    for i in arr:
        print(i, end=" ")
