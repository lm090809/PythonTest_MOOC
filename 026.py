n = int(input())
hour = 0
max_hour = 0
for n in range(n):
    s = input().split()
    if 140 >= int(s[0]) >= 90 >= int(s[1]) >= 60:
        hour = hour+1
        if hour >= max_hour:
            max_hour = hour
        #print("hour = %d" %hour)
        #print("max_hour = %d" % max_hour)
    else:
        hour = 0

print(max_hour)

