s = input()
arr2 = []
c = 0
for i in s:
    c += 1
    if "f" == i:
        arr2.append(c)
if len(arr2) == 1:
    print(arr2[0] - 1)
elif len(arr2) > 1:
    print(arr2[0] - 1, end=(" "))
    print(arr2[-1] - 1)
else:
    print()
