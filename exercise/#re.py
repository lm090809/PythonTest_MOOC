import re
def match(pattern, string):
    x = re.match(pattern, string)
    if x != None:
        print(x.group())
    else:
        print("None")

match("a c", "a cdkgh")