n = int(input())
sum = 0
for i in range(n - 1):
    a = int(input())
    sum += a
print(int(n * (n+1) / 2) - sum)
