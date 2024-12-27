a = input().split()
x,y=int(a[0]), int(a[1])
if 1 >= x >= -1:
    if 1 >= y >= -1:
        print("yes")
    else:
        print("no")
else:
    print("no")