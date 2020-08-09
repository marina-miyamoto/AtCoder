import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

K = int(input())
answer = 0
for i in range(1,K+1):
    for j in range(1,K+1):
        for h in range(1,K+1):
            answer += gcd(i,j,h)
print(answer)
