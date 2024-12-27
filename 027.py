s = input()
n = len(s)
m = 0
r=""

for i in range(n-1,-1,-1):
    if s[i] == "0":
        continue
    elif s[i] !="0":
        m = i
        break

for i in range(m,-1,-1):
    if s[i] == "-":
        r = s[i] + r
    else:
        r = r + s[i]

if s == "0":
    r = s
print(r)






