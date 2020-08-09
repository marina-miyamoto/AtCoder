"""

lake, houses = list(map(int, input().split()))
distances = list(map(int, input().split()))
if distances[0] == 0:
    answer = min(distances[-1] - distances[0], abs(distances[-1] - distances[1]))
else:
    answer = distances[-1] - distances[0]
print(answer)

"""


[k,n] = list(map(int, input().split()))
 
li = list(map(int, input().split()))
 
distances = []
for i in range(n):
    if i == 0:
        distances.append(li[n-1] - li[i])
    else:
        distances.append(k - (li[i] - li[i-1]))

print(distances)
print(min(distances))
