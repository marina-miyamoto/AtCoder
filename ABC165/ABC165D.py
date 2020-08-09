import math
A,B,N = list(map(int, input().split()))
answer = (math.floor((A*N)/B)) - A * math.floor(N/B)
print(answer)


import math
A,B,N = list(map(int, input().split()))
a = 0
for i in range(1, N+1):
    answer = (math.floor((A*i)/B)) - A * math.floor(i/B)
    a = max(a, answer)
print(a)
