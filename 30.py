def f(a,b):
    if a%b==0:
        return b
    elif a>b:
        return f(b,a%b)
    else:
        return f(b,a)

s = input().split()
a, b = int(s[0]), int(s[1])
print(f(a,b))

