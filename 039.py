def cal(s):
    s1, s2 = s[0], s[1]
    t = 0
    send_out = -1
    if s1.find(s2) == -1:
        #print(s1.find(s2))
        print("no")
    else:
        for j in range(len(s1)):
            re = s1.find(s2, t)
            t = t + len(s2)
            if re == -1:
                break
            elif re != send_out:
                print(re, end=" ")
                send_out = re

n = int(input())
for i in range(n):
    print("\n")
    s = input().split()
    cal(s)

