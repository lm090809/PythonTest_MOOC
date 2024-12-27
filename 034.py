s = input()
for c in s:
    if "a" <= c <= "z": #lower
        print(c.upper(), end="")
    elif "A"<=c<="Z": #upper
        print(c.lower(), end="")
    else:
        print(c, end="")


