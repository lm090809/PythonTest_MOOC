n = int(input())
a,b,c = 0,0,0
for n in range(n):
    s = input().split()
    a += int(s[0])
    b += int(s[1])
    c += int(s[2])
sum = a+b+c
print(a,b,c,sum)
