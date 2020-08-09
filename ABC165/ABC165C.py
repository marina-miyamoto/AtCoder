import itertools
N, M, Q = list(map(int, input().split()))
for  i in itertools.combinations_with_replacement(range(1,M+1), N):
    print(i)








# points = []
# for i in range(Q):
#     point = list(map(int, input().split()))
#     points.append(point)
    
# answers = []
# answer = [0] * N
# for j in range(len(points)):
#     for k in range(1, M+1):
#         #answer = [0] * N
#         if k + points[j][2] <= M:
#             answer[points[j][1]-1] = points[j][2] + k
#             answer[points[j][0]-1] = k
#             answer.append(points[j][3])
            
#             answers.append(answer)
# print(answers)

# for l in range(len(answers)):
#     

