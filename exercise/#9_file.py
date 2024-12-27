try:
    f = open("C:\\02 Software\\PythonTest\\exercise\\t.txt","a")
    f.write("append content: yeah\n")
    f.write("end\n")
    f.close()

    f1 = open("C:\\02 Software\\PythonTest\\exercise\\t.txt", "r")
    lines = f1.readlines()
    f.close()
    for x in lines:
        print(x, end="")
except Exception as e:
    print(e)

try:
    f = open("C:\\02 Software\\PythonTest\\exercise\\t1.txt","r+")
    f.write("hello\n")
    f.write("end\n")
    lines = f.readlines()
    f.close()
    print(type(lines))
    for x in lines:
        print(x, end="")
except Exception as e:
    print(e)