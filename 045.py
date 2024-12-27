s = input().split()
n, m, k = int(s[0]), int(s[1]), int(s[2])
A = []
B = []
C = []
for i in range(n):
    lst = list(map(int, input().split()))
    A.append(lst)
for j in range(m):
    lst = list(map(int, input().split()))
    B.append(lst)
for i in range(n):
    C.append([0] * k)
#print(A)
#print(B)
#print(C)

for n in range(n):
    #print("n=",n)
    for p in range(k):
        #print("k=",p)
        sum = 0
        for i in range(m):
            #print("m=",i)
            sum += A[n][i] * B[i][p]
        C[n][p] = sum
        #print("C=",C[n][p])
        print(C[n][p], end=" ")
    print("")



