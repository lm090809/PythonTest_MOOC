'''
程序1：统计单词词频
命令行运行
'''
import sys
import re
for x in sys.argv:
    print(x)

print("two file is ",sys.argv[1], sys.argv[2])
lines = []
word = []
word_dict ={}
word_str = ""
try:
    input_file = open(sys.argv[1], "r")
    lines = input_file.readlines()
    input_file.close()
    print(lines)
    print(type(lines))
except Exception as e:
    print(e)

word = re.split(";| |,|\*|\n|\?|\]|\.|\'|\[|\:",str(lines))
for x in word:
    print(x)
    if x == "":
        pass
    elif x not in word_dict:
        word_dict[x]= 1
    else:
        word_dict[x] +=1
print("word_dict=", word_dict)

for k,v in word_dict.items():
    word_str += k + " " + str(v) + "\n"
print("word_str=", word_str)

try:
    output_file = open(sys.argv[2], "w")
    output_file.write(word_str)
    output_file.close()

except Exception as e:
    print(e)





