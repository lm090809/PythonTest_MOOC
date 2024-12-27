import math
x = input().split()
a, b = int(x[0]), x[1]
if a <= 1000:
    y = 8
else:
    y = 8 + math.ceil((a-1000)/500)*4

if b == "y":
    y = 5+y

print(y)