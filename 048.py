import re
#48
# m = "[0-9]\d*|0"

#49
m="[0-9]\d*\.?\d*"

while True:
    try:
        s = input()
        lst = re.findall(m,s)
        for x in lst:
            print(x)
    except:
        break