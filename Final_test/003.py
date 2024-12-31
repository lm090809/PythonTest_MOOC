n = int(input())
for i in range(0,n):
    char = input().lower()
    s = input().lower().split()
    for w in s:
        count = w.count(char)
        print(count, end=" ")
    # print("\n")

