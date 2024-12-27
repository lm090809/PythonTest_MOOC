n = int(input())
lst = []
for i in range(n):
    s = input().split()
    lst.append((s[0], int(s[1])))
lst.sort(key = lambda x:(-x[1],x[0]) )
for l in lst:
    print(l[0],l[1])