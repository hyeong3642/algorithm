from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = []
    queue = deque()
    for i in range(n):
        tmp = list(map(int, input().split()))
        graph.append(tmp)
        for j in range(m):
            if tmp[j] == 1:
                queue.append((i, j, 0))
    for i in range(n):
        for j in range(m):
            if graph[i][j]== 1:
                queue.append((i, j, 0))
    day =0
    while queue:
        x, y, time = queue.popleft()
        if x-1 >= 0 and graph[x-1][y] == 0:
            graph[x-1][y] =1
            queue.append((x-1,y,time+1))
        if x+1 < n and graph[x+1][y] == 0:
            graph[x+1][y] =1
            queue.append((x+1,y,time+1))
        if y-1 >= 0 and graph[x][y-1] == 0:
            graph[x][y-1] =1
            queue.append((x,y-1,time+1))
        if y+1 < m and graph[x][y+1] == 0:
            graph[x][y+1] =1
            queue.append((x,y+1,time+1))
        ans = time
    check = 0
    for i in range(n):
        if 0 in graph[i]:
            check = 1
            break
    if check == 1:
        print("-1")
    else:
        print(ans)
        