x = int(input())
arr = []

while x != 0:
    arr.append(x)
    x = int(input())

s = sum(arr) / len(arr)
ss = 0
for i in arr:
    ss += (i - s) ** 2
ss = (ss / (len(arr) - 1)) ** 0.5

print(ss)
