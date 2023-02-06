s = input()
b = ""
a = ""
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
for i in range(len(s)):
    if i % 2 == 0:
        a = a + s[i]
    else:
        b += s[i]
print(a)
print(b)
arr = list(s)
arr.reverse()
s = ''
a = ''
for i in range(len(arr)):
    s += arr[i]
    if i % 2 == 0:
        a += arr[i]
print(s)
print(a)
print(len(s))

