import math
goal = int(input())
money = 100
count = 0
while money < goal:
    money = math.floor(money * 1.01)
    count += 1
print(count)