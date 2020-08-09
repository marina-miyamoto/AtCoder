import collections
workers = int(input())
A = list(map(int, input().split()))
new = collections.Counter(A)
for i in range(1,workers+1):
    print(new[i])

