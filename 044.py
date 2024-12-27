n = int(input())
lst = []
for i in range(n):
    s = input().split()
    lst.append([i,s[0],int(s[1])])

def myKey(x):
    if x[2]>=60:
        pass
    else:
        x[2] = 59
    return(-x[2],x[0])

lst.sort(key = myKey)
for x in lst:
    print(x[1])


