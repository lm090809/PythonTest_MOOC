import math
s = input().split()
h, r = int(s[0]), int(s[1])
Pi = 3.14159
V = Pi * r * r * h
t = math.ceil(20*1000/V)
print(t)