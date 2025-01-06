import re
n = int(input())
m = r"<([1-9]\d{0,2}|0)>"
for i in range(n):
        # print(i)
        s = input()
        lst = re.findall(m,s, flags=0)
        if lst != []:
            for x in lst:
                print(x, end=" ")
            print()
        else:
            print("NONE")


