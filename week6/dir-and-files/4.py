import os

path = "a.txt"
cnt = 0
a = open('a.txt', 'r')
for lines in a:
    cnt += 1
print(cnt)
