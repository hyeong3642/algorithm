from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())

for i in range(t):
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(str, input().split())))
    visit = [[0] * n for _ in range(n)]
    queue = deque()
    visit[n-1][0] = 1
    queue.append((n-1, 0))
    while queue:
        x, y = queue.popleft()
        ## 1번
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny <n and graph[nx][ny] == 'H':
                if visit[nx][ny] == 0:
                    visit[nx][ny] = visit[x][y]+1
                    queue.append((nx, ny)) 
        ## 3번
        if x-2 >=0 and graph[x-1][y] == '.' and graph[x-2][y] == 'H':
            if visit[x-2][y] == 0 :
                visit[x-2][y] = visit[x][y] +1
                queue.append((x-2, y))
            elif visit[x-2][y] > visit[x][y]+1 :
                visit[x-2][y] = visit[x][y] +1
                queue.append((x-2, y))
        ## 4번
        if x-1 >= 0 and y-1 >= 0 and graph[x-1][y] == '.' and graph[x][y-1] == '.' and graph[x-1][y-1] == 'H':
            if visit[x-1][y-1] == 0 :
                visit[x-1][y-1] = visit[x][y] +1
                queue.append((x-1, y-1))
            elif visit[x-1][y-1] > visit[x][y]+1:
                visit[x-1][y-1] = visit[x][y]+1
                queue.append((x-1, y-1))
        ## 5번
        if x-1 >= 0 and y+1 <n and graph[x-1][y] == '.' and graph[x][y+1] == '.' and graph[x-1][y+1] == 'H':
            if visit[x-1][y+1] == 0 :
                visit[x-1][y+1] = visit[x][y] +1
                queue.append((x-1, y+1))
            elif visit[x-1][y+1] > visit[x][y]+1:
                visit[x-1][y+1] = visit[x][y] +1
                queue.append((x-1, y+1))
        ## 2번 2칸
        if y+2 <n and x-1>=0 and graph[x][y+1] == '.' and graph[x][y+2] == 'H' and graph[x-1][y] == '.' and graph[x-1][y+1] == '.' and graph[x-1][y+2] == '.':
            if visit[x][y+2] == 0 :
                visit[x][y+2] = visit[x][y] +1
                queue.append((x, y+2))
            elif visit[x][y+2] > visit[x][y]+1:
                visit[x][y+2] = visit[x][y]+1
                queue.append((x, y+2))
        
        if y-2 >=0 and x-1>=0 and graph[x][y-1] == '.' and graph[x][y-2] == 'H' and graph[x-1][y] == '.' and graph[x-1][y-1] == '.' and graph[x-1][y-2] == '.':
            if visit[x][y-2] == 0 :
                visit[x][y-2] = visit[x][y] +1
                queue.append((x, y-2))
            elif visit[x][y-2] > visit[x][y]+1 :
                visit[x][y-2] = visit[x][y] +1
                queue.append((x, y-2))
        ## 2번 3칸
        if y+3 <n and x-1>=0 and graph[x][y+1] == '.' and graph[x][y+2] == '.' and graph[x][y+3] == 'H' and graph[x-1][y] == '.' and graph[x-1][y+1] == '.' and graph[x-1][y+2] == '.' and graph[x-1][y+3] == '.':
            if visit[x][y+3] == 0 :
                visit[x][y+3] = visit[x][y] +1
                queue.append((x, y+3))
            elif visit[x][y+3] > visit[x][y]+1:
                visit[x][y+3] = visit[x][y]+1
                queue.append((x, y+3))    
        if y-3 >=0 and x-1>=0 and graph[x][y-1] == '.' and graph[x][y-2] == '.' and graph[x][y-3] == 'H' and graph[x-1][y] == '.' and graph[x-1][y-1] == '.' and graph[x-1][y-2] == '.' and graph[x-1][y-3] == '.':
            if visit[x][y-3] == 0 :
                visit[x][y-3] = visit[x][y] +1
                queue.append((x, y-3))
            elif visit[x][y-3] > visit[x][y]+1 :
                visit[x][y-3] = visit[x][y]+1
                queue.append((x, y-3))
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'H' and visit[i][j] == 0:
                visit[i][j] = -1
    for i in range(n):
        for j in range(n):
            print(visit[i][j], end =' ')
        print("")