n = int(input())
lst_a = input().split()
lst_b = input().split()
sum = 0
for i in range(n):
    sum+= int(lst_a[i]) * int(lst_b[i])

print(sum)