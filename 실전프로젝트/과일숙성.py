from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = []
    queue = deque()
    for i in range(n):
        graph.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(m):
            if graph[i][j]== 1:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <n and 0<= ny < m and graph[nx][ny] ==0:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))
    ans = 0
    check = 0
    for i in range(n):
        if 0 in graph[i]:
            check = 1
            break
        ans = max(ans, max(graph[i])) 
    if check == 1:
        print("-1")
    else:
        print(ans-1)
        