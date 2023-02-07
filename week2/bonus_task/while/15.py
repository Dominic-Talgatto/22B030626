a = 0
b = 1
c = 0
cnt = 0
m = int(input())
arr = []
arr.append(a)
arr.append(b)
for i in range(45):
    c = a + b
    arr.append(c)
    a = b
    b = c
for i in range(len(arr)):
    if arr[i] == m:
        print(i)
        t = True
if not t:
    print(-1)
        
