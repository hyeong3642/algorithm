from collections import deque
import math

t = int(input())

for i in range(t):
    n, m, d = map(int,input().split())
    lad = []
    for i in range(m):
        lad.append(input())
    lad.reverse()
    now = d*2-2
    idx = 0
    for i in range(0, m):
        if 0 <(now) and lad[i][now-1] == "+":
            now -= 2
        elif (now)<n*2-2 and lad[i][now+1] == "+":
            now += 2
        if lad[i][now] == '?':
            idx = i+1
            break
    left = now-2
    right = now+2
    ans = []
    for i in range(idx,m):
        if 0 <(now)and lad[i][now-1] == "+":
            now -= 2
        elif  (now)<n*2-2 and lad[i][now+1] == "+":
            now += 2
    if left >= 0:
        for i in range(idx,m):
            if 0 <(left) and lad[i][left-1] == "+":
                left -= 2
            elif (left)<n*2-2 and lad[i][left+1] == "+":
                left += 2
        ans.append((left/2+1))
    if right <= n*2-2:
        for i in range(idx, m):
            if 0 <(right)and lad[i][right-1] == "+":
                right -= 2
            elif (right)<n*2-2 and lad[i][right+1] == "+":
                right += 2
        ans.append((right/2+1))
    ans.append((now/2+1))
    ans.sort()
    ans2 = ''
    for i in range(len(ans)):
        ans2 += str(int(ans[i]))
        ans2 += ' '
    print(ans2)
    
