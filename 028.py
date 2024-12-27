n7 = 300
n9 = 0
n10 = 0
while n7>0:
    #print("n7=%d" % n7)
    s = str(n7)
    a0, a1, a2 = int(s[2]), int(s[1]), int(s[0])
    n10 = a0 * 1 + a1 * 7 + a2 * 49
    n9 = a2 * 1 + a1 * 9 + a0 * 81
    #print("n10=%d,n9=%d" % (n10, n9))
    if n10 != n9:
        n7 =  n7+1
    else:
        print(n10)
        print(str(a2) + str(a1) + str(a0))
        print(str(a0)+str(a1)+str(a2))
        break












