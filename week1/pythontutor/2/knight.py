a = int(input())
b = int(input())
c = int(input())
d = int(input())

if abs(a-c) == 2:
    if abs(b-d) == 1:
        print("YES")
    else: print("NO")
elif abs(b-d) == 2:
    if abs(a-c) == 1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
