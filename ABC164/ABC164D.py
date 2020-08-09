S = list(map(str,input()))
answers = []
if len(S) < 4:
    print(0)
    exit()

for i in range(len(S)):
    for j in range(i+4, len(S)+1):
        if int(''.join(S[i:j])) % 2019 == 0:
            answers.append(int(''.join(S[i:j])))
print(len(answers))
