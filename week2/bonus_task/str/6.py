s = input()
arr2 = []
c = 0
for i in s:
    c += 1
    if "f" == i:
        arr2.append(c)
        if len(arr2) == 2:
            break
if len(arr2) == 0:
    print(-2)
elif len(arr2) == 1:
    print(-1)
else:
    print(arr2[-1] - 1)
