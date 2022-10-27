from collections import deque

t= int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]
for i in range(t):
    n,m = map(int, input().split())
    
    d=[]
    for i in range(n):
        d.append(list(map(int,input())))
    def bfs(x, y):
        queue = deque()
        queue.append((x,y))
        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and d[nx][ny] == 1:
                    queue.append((nx, ny))
                    d[nx][ny] = d[x][y] + 1
                    #print(queue)
        #print(d)
        return d[n-1][m-1]
    #print(d)
    print(bfs(0,0))