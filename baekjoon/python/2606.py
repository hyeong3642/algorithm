com = int(input())
numedge = int(input())

graph = [[]*com for _ in range(com+1)]
for i in range(numedge):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
#print(graph)
count = 0
visit = [0] * (com+1)
def dfs(start):
    global count
    visit[start] = 1
    for i in graph[start]:
        if visit[i] == 0:
            dfs(i)
            count +=1
dfs(1)
print(count)