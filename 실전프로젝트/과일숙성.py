t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    check = 0
    time = 0
    while check == 0:
        visited = [[0] * m for _ in range(n)]
        tmp = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0 :
                    tmp = -1
        if tmp == 0 :
            print(time)
            break
        else : 
            time +=1
            if time > m+1:
                print("-1")
                break
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 1 and visited[i][j] == 0:
                    if i-1 >=0 and graph[i-1][j] == 0:
                        graph[i-1][j] = 1
                        visited[i-1][j] = 1
                    if i+1 <n and graph[i+1][j] == 0 :
                        graph[i+1][j] = 1
                        visited[i+1][j] = 1
                    if j-1 >=0 and graph[i][j-1] == 0 :
                        graph[i][j-1] = 1
                        visited[i][j-1] = 1
                    if j+1< m and graph[i][j+1] == 0:
                        graph[i][j+1] = 1
                        visited[i][j+1] = 1
        