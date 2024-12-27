s = input()
lst = []
for i in range(0,len(s)-1):
    for j in range(2,len(s)-i+1):
        s_sub = s[i:i+j]
        if s_sub == s_sub[::-1]:
            lst.append([len(s_sub),i,s_sub])
lst.sort()
for l in lst:
    print(l[2])

