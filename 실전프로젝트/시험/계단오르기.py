t = int(input())

for i in range(t):
    stair = list(map(int, input().split()))
    obs = stair[1:]
    cur = 0
    last = stair[0]
    ans = 0
    while cur<last:
        if cur+2 not in obs:
            cur +=2
            ans +=1
        else :
            cur +=1
            ans +=1
    print(ans)

