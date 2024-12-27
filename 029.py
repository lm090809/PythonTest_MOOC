L,R = input().split()
count = 0
for n in range(int(L),int(R)):
    for c in str(n):
        if c == "2":
            count+=1
for c in R:
    if c == "2":
        count += 1
print(count)





