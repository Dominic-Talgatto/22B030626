b = int(input())
sum = 0

for i in range(1, b+1):
    if i == 1:
        fact = 1
    else:
        fact = fact * i
    sum += fact

print(sum)
