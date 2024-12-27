import math
s = input().split()
n,x,y = int(s[0]), int(s[1]), int(s[2])
n -= math.ceil(y/x)
if n <= 0:
    n = 0
print(n)
