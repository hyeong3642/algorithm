from collections import deque

city, street = map(int, input().split())
graph = [[] for _ in range(city + 1)]

for _ in range(street):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

start, end = map(int, input().split())
low, limit = 0, 1000000000
weight = 0
def bfs(mid):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        now = q.popleft()
        if now == end:
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