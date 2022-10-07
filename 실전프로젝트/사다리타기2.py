from collections import deque

t = int(input())

for i in range(t):
    n, m, d = map(int,input().split())
    lad = []
    for i in range(m):
        lad.append(input())
        lad[i] = lad[i].replace("?", "+")
    lad.reverse()
    now = d*2-2
    
    print(lad)
