s = input()
a = ''
arr2 = []
c = 0
for i in s:
    if i == 'h':
        arr2.append(c)
    c += 1
for i in range(len(s)):
    if s[i] == 'h' and i != arr2[0] and i != arr2[-1]:
        print(s[i].upper(), end=(''))
    else:
        print(s[i], end=(''))
