from collections import defaultdict

N, M = list(map(int, input().split()))
height = list(map(int, input().split()))
roads = defaultdict(list)
answer = 0
for i in range(M):
    a, b = list(map(int, input().split()))
    roads[a].append(b)
    roads[b].append(a)
for j in range(1, N+1):
    heights = []
    heights.append(height[j-1])
    for k in range(len(roads[j])):
        heights.append(height[roads[j][k]-1])
    if len(heights) == 1:
        answer += 1
    elif max(heights) == height[j-1] and len(set(heights)) != 1: 
        answer += 1

print(answer)

