s = input().split()
n,m = int(s[0]), int(s[1])
supply_dict = {}
purchase_dict = {}
sum = 0
for m in range(m):
    cai = input().split()
    supply_dict[cai[0]] = [int(cai[1]),int(cai[2])]
for n in range(n):
    cai = input().split()
    for c in cai:
        #print(supply_dict[c])
        if supply_dict[c][1] > 0:
            if c in supply_dict.keys():
                supply_dict[c][1] -= 1
                sum += supply_dict[c][0]
print(sum)
