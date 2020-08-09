N = int(input())
S = input()
R  = list()
B = list()
G = list()

answer = 0

for i in range(len(S)):
    if S[i] == "R":
        R.append(i)
    elif S[i] == "B":
        B.append(i)
    else:
        G.append(i)

for j in range(len(R)):
    for k in range(len(B)):
        

