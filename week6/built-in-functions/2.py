str = input()
l = 0
u = 0
for chr in str:
    if chr.islower():
        l += 1
    if chr.isupper():
        u += 1

print(f"lower: {l}\nupper: {u}")
