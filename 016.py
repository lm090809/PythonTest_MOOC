x =float(input())
y =0
if 0<=x<5:
    y = -x+2.5
elif 5<=x<10:
    y = 2-1.5*(x-3)*(x-3)
elif 10<=x<20:
    y = x/2-1.5

print("%.3f" % y)
