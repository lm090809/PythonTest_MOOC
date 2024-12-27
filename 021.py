n = int(input())
total = 0
everage = 0
for i in range(n):
    total += int(input())
everage = total/n
print(total, "%.5f" % everage)