N, K = list(map(int, input().split()))
if K == 1:
    print(0)
elif (N % 2 == 0 and K % 2 == 0):
    if N % K == 0:
        print(0)
    else:
        print(2)
else:
    while N > abs(N - K):
        N = abs(N - K)
    print(N)




#Right Answer
N, K = list(map(int, input().split()))
answer = N % K
print(min(answer, abs(K - answer)))