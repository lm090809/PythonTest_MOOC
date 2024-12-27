n = int(input())
s1 = input().split()
rate = int(s1[1])/int(s1[0])
for n in range(1,n):
    s2 = input().split()
    rate_other = int(s2[1])/int(s2[0])
    diff = rate_other - rate
    if diff > 0.05:
        print("better")
    elif diff < -0.05:
        print("worse")
    else:
        print("same")
