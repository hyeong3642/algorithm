import math

t=int(input())
for i in range(t):
    n = int(input())
    dp = [0] * 101
    ans = 0
    for i in range(n):
        a,c = map(int, input().split())
        if dp[a]!= 0:
            if not (dp[a]==1 and c ==1) and dp[a] + c > 2**math.ceil(math.log2(dp[a])):
                ans += dp[a]
        dp[a] +=c
    print(ans)