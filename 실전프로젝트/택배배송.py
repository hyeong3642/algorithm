from collections import deque

t = int(input())
for i in range(t):
    city,street, anum, bnum = map(int, input().split())
    graph = [[] for _ in range(city + 1)]

    for _ in range(street):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    low, limit = 0, 10000
    weight = 0

    def bfs(mid):
        q = deque()
        q.append(anum)
        visited[anum] = True
        while q:
            now = q.popleft()
            if now == bnum:
                return True
            for node, cost in graph[now]:
                if not visited[node] and mid <= cost:
                    q.append(node)
                    visited[node] = True
        return False

    while low <= limit:
        mid = (low + limit) // 2
        visited = [False for _ in range(city + 1)]
        if bfs(mid) == True:
            weight = max(weight, mid)
            low = mid + 1
        else:
            limit = mid - 1
    print(weight)
