summer, homework = list(map(int, input().split()))
A = list(map(int, input().split()))
if summer-sum(A)>=0:
    print(summer-sum(A))
else:
    print(-1)