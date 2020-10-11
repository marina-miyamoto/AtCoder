start, move, distance = list(map(int, input().split()))
if abs(start) > abs(distance) and abs(start) // abs(distance) <= abs(move):
    n = abs(start) // abs(distance)
    print(abs(start) - (abs(distance) * n))
elif abs(start) > abs(distance) and abs(start) // abs(distance) > abs(move):
    n = abs(start) // abs(distance)
    print(abs(start) - (abs(distance) * abs(move)))
else:
    print(abs(start))
