N, K = list(map(int, input().split()))
snack = []
for i in range(K):
    number = int(input())
    s = list(map(int, input().split()))
    for j in range(len(s)):
        snack.append(s[j])

answer = 0
for i in range(1, N+1):
    if i not in snack:
        answer += 1

print(answer)