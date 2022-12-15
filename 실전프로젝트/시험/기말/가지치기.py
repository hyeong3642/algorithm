t = int(input())

def delete(d, node):
    node[d] = -2
    for i in range(len(node)):
        if d == node[i]:
            delete(i, node)

for i in range(t):
    n, d = map(int, input().split())
    node = list(map(int, input().split()))
    ans = 0
    delete(d, node)
    for i in range(n):
        if node[i] != -2 and i not in node:
            ans +=1
    print(ans)
