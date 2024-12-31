import re

m=""
while True:
    try:
        s = input()
        if re.match(m,s) != None:
            print("yes")
        else:
            print("no")
    except:
        break