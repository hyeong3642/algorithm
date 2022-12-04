from collections import deque

t = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(t):
    n, d = map(int, input().split())
    r, c = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    visited = [[0] * n for _ in range(n)]
    visited[r][c] = 1
    count = 1
    while True :
        check = 0
        for _ in range(4):
            d = (d+3)%4
            nr = r + dx[d]
            nc = c + dy[d]

            if 0<=nr < n and 0 <= nc < n and graph[nr][nc]== 0:
                if visited[nr][nc] ==0:
                    visited[nr][nc] = 1
                    count +=1
                    r = nr
                    c = nc
                    check =1
                    break
        if check == 0 :
            if graph[r-dx[d]][c-dy[d]] == 1:    
                print(count)
                break
            else: 
                r = r-dx[d]
                c = c-dy[d]