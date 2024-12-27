x = input().split()
a,b,c = int(x[0]), int(x[1]), int(x[2])
if a+b>c and a+c>b and b+c>a:
    print("yes")
else:
    print("no")