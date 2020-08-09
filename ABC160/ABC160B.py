X = int(input())
answer = (X // 500) * 1000
new_X = X % 500
answer += (new_X // 5) * 5
print(answer)