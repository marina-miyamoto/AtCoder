
K = int(input())
S,E = list(map(int, input().split()))
answer = "NG"
for i in range(S, E+1):
    if i % K == 0:
        answer = "OK"
print(answer)