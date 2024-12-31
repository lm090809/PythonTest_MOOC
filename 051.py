import re
# n.I.O
m=r"[a-zA-Z][a-zA-Z0-9_\-]{7,}"

while True:
    try:
        s = input()
        if re.match(m,s) != None:
            print("yes")
        else:
            print("no")
    except:
        break