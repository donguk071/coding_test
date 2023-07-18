import sys

# 문제가 설명이 굉장히 이상하다. 건너갈수있는 가지수를 찾는 문제이다.

N = int(sys.stdin.readline().split())
rocks = list(map(int , sys.stdin.readline().split()))

dp = [1]*N # 동적배열을 만들어 위값을 재해석하여 넣어준다. 
count = 0

for i in range(1, N):
    find = 0
    for j in range(i):
        if rocks[j] < rocks[i]:
            find = max(find, dp[j])
    dp[i] = find + 1
    
print(max(dp))