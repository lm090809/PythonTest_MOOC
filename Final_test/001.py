n = int(input())
if n%5 == 0 and n%7==0:
    print("best")
elif n%7 !=0 and n%5 == 0:
    print("good")
else:
    print("bad")