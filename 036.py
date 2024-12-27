s = str(input())
i = 0
l = "no"
for i in range(len(s)):
    if s[i] in s[:i]:
        continue
    elif s[i] in s[i+1:]:
        continue
    else:
        l = s[i]
        break
print(l)




