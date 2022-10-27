from collections import deque

t = int(input())

def bfs(mid):
        q = deque()
        q.append(A)
        visited[A] = True
        while q :
            now = q.popleft()
            if now == B:
                return True
            for node, cost in graph[now]:
                if not visited[node] and mid <= cost:
                    q.append(node)
                    visited[node] = True
        return False
for i in range(t):
    N, M, A, B = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        O, D, C = map(int, input().split())
        graph[O].append((D,C))
        graph[D].append((O,C))
    low = 0
    limit = 10000
    weight = 0
    
    while low<=limit :
        mid = (low + limit) //2
        visited = [False for _ in range(N+1)]
        if bfs(mid) == True:
            weight = max(weight, mid)
            low = mid +1
        else :
            limit = mid -1
    print(weight)
    
