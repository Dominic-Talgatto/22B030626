s = input()
a = ''
arr2 = []
c = 0
for i in s:
    if i == 'h':
        arr2.append(c)
    c += 1
for i in range(len(s)):
    if  arr2[0] <= i <= arr2[-1]:
        a = s[i] + a

print(s[: arr2[0]] + a + s[arr2[-1] + 1 : ])
