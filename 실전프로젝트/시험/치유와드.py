t = int(input())

for i in range(t):
    n, m = map(int,input().split())
    a, b = map(int, input().split())
    graph = [[0]*n for _ in range(n)]
    dead = []
    ward = []
    for i in range(a):
        r, c = map(int, input().split())
        dead.append((r,c))
    for i in range(b):
        r, c = map(int, input().split())
        ward.append((r,c))
    for r,c in dead:
        for x in range(0,n):
            for y in range(0,n):
                if max(abs(x-r),abs(y-c))-m-1<0 :
                    if x==r and y == c:
                        graph[x][y] += max(abs(x-r),abs(y-c))-m
                    else:
                        graph[x][y] += max(abs(x-r),abs(y-c))-m-1
    for r,c in ward :
        for x in range(0,n):
            for y in range(0,n):
                if m-(abs(x-r)+abs(y-c))+1 >0 :
                    if x==r and y == c:
                        graph[x][y] += m-(abs(x-r)+abs(y-c))
                    else:
                        graph[x][y] += m-(abs(x-r)+abs(y-c))+1
    for i in range(0, n):
        for j in range(0,n):
            print(graph[i][j], end = ' ')
        print("")