A,B,C,D = list(map(int, input().split()))
a = C - B
t = A - D
while t > 0 and a > 0:
    a -=  B
    t -= D
if a <= 0:
    print('Yes')
else:
    print("No")