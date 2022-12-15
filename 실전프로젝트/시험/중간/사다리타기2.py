t = int(input())
for i in range(t):
    n, m, d = map(int, input().split())
    ladder = []
    for i in range(m):
        ladder.append(input())
    ladder.reverse()
    now = d*2-2
    idx = 0
    for i in range(0, m):
        if 0<now and ladder[i][now-1] == "+":
            now -=2
        if now<n*2-2 and ladder[i][now+1] == "+":
            now +=2
        if ladder[i][now] == "?":
            idx = i+1
            break
    ans =[]
    left = now -2
    right = now +2
    for i in range(idx, m):
        if 0<now and ladder[i][now-1] == "+":
            now -=2
        elif now<n*2-2 and ladder[i][now+1] == "+":
            now +=2
    ans.append((now+2)//2)
    if left >= 0:
        for i in range(idx, m):
            if 0<left and ladder[i][left-1] == "+":
                left -=2
            if left<n*2-2 and ladder[i][left+1] == "+":
                left +=2
        ans.append((left+2)//2)
    if right <= n*2-2:
        for i in range(idx, m):
            if 0<right and ladder[i][right-1] == "+":
                right -=2
            if right<n*2-2 and ladder[i][right+1] == "+":
                right +=2
        ans.append((right+2)//2)
    print(ans)