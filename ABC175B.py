import bisect
N = int(input())
L = sorted(set(map(int,input().split())))
print(len(L))
count = 0
tri = []
for i in range(N-2):
    k = i + 2
    for j in range(i+1, N):
        while (k < N and L[i] + L[j] > L[k]):
            k += 1
        if k > j:
            count += k - j - 1
print(count)
