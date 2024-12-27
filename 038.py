S = input().split(",")
S,S1,S2 = S[0],S[1],S[2]
S2_point=S.rfind(S2)
S1_point=S.find(S1)
#print(S2_point)
#print(S1_point)
if S2_point == -1 or S1_point == -1:
    print("-1")
elif S2_point-S1_point-len(S1) < 0:
    print("-1")
else:
    print(S.rfind(S2)-S.find(S1)-len(S1))