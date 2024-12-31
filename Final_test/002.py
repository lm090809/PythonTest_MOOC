s = input().split()
# print(s)
sum = 0
for i in s:
    if int(i)<=60:
        sum += int(i)
print(sum)