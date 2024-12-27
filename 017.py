s = input().split()
x,y,z = int(s[0]), int(s[1]), s[2]
if z not in ["+", "-", "*", "/"]:
    m = "Invalid operator!"
else:
    if z == "+":
        m = x+y
    elif z == "-":
        m = x-y
    elif z == "*":
        m = x*y
    elif z== "/":
        if y == 0:
            m = "Divided by zero!"
        else:
            m = x//y
print(m)



