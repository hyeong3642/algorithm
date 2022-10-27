t = int(input())

for i in range(t):
    n = int(input())
    graph = [[0]*2 for _ in range(101)]
    ans = 0
    for j in range(n):
        a, c = map(int, input().split())
        sq = 2
        if graph[a][1] == 0 :
            while sq <= c:
                sq *=2
            graph[a][0] +=c
            graph[a][1] = sq
        elif (graph[a][0] + c) > graph[a][1]:
            ans += graph[a][0]
            graph[a][0] +=c
            while graph[a][1] <= graph[a][0]:
                graph[a][1] *=2
        else :
            graph[a][0] +=c
    print(ans)