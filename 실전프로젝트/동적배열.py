t = int(input())

for i in range(t):
    n = int(input())
    graph = [[] for i in range(100)]
    ans = 0
    for j in range(n):
        a, c = map(int, input().split())
        count = 0
        for i in range(len(graph[a])):
            if graph[a][i] !=0  :
                count +=1
        if c + count <=len(graph[a]):
            for i in range(count, count+c) :
                graph[a][i] = 1
        else :
            tmp = count + c
            sq = 1
            while sq<= tmp:
                sq = sq*2
            if len(graph[a]) == 0:
                graph[a] = [0] *sq
                for i in range(tmp):
                    graph[a][i] = 1
            else :
                change = [0] * sq
                for i in range(tmp):
                    change[i] = 1
                    ans +=1
                ans -= c
                graph[a] = change
    print(ans)
