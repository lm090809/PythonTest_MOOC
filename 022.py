n = int(input())
s = input().split()
max = int(s[0])
min = int(s[0])
for n in range(n):
    if int(s[n])>=max:
        max = int(s[n])
    elif int(s[n])<=min:
        min = int(s[n])
diff = max -min
print(diff)