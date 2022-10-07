from collections import deque

t = int(input())

for i in range(t):
    n, m, d = map(int,input().split())
    lad = []
    for i in range(m):
        lad.append(input())
    lad.reverse()
    now = d*2-2
    for i in range(1, m):
        if 0 <(now-1)<n*2-2 and lad[i][now-1] == "+":
            now -= 2
        elif 0< (now+1)<n*2-2 and lad[i][now+1] == "+":
            now += 2
    print(str((now+2)//2))
