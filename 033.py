s = input()
i = 0
for c in s:
    if c.isdigit():
        i+=1
    else:
        continue
print(i)