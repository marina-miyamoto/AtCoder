N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
A = sorted(A, reverse=True)
for i in range(M):
    if A[i] < sum(A) * (1/ (4*M)):
        print("No")
        exit()
print("Yes")