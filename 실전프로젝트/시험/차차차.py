t = int(input())
for i in range(t):
    N = int(input())
    graph = [[0, 0, 0, 0, 0] for _ in range(N+1)]
    for i in range(N,0, -1):
        graph[i] = list(map(int, input().split()))
    score = [[0, 0, 0, 0, 0] for _ in range(N+1)]
    score[0] = [-1, -1, 0, -1, -1]

    for x in range(1, N+1):
        for y in range(5):
            if graph[x][y] == 1:
                score[x][y] = -1
                continue
            
            score[x][y] = score[x-1][y]
            score[x][y] = max(score[x][y], score[x-1][y-1]) if y>0 else score[x][y]
            score[x][y] = max(score[x][y], score[x-1][y+1]) if y<4 else score[x][y]

            score[x][y] += graph[x][y] if graph[x][y] >1 else 0
            score[x][y] +=1 if y>0 and graph[x][y-1] ==1 else 0
            score[x][y] += 1 if y<4 and graph[x][y+1] == 1 else 0
    print(max(score[N]))
