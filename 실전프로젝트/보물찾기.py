t = int(input())

for i in range(t):
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(input().split())
    visited = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
    start = graph[0][0]
    a = start[0]
    b = start[1]
    beforea = 'B'
    visited[0][0].append('B')
    x=0
    y=0
    while True:
        if beforea == 'F':
            if a == 'F':
                x+=int(graph[x][y][1])
                beforea = 'F'
                if beforea in visited[x][y]:
                    print(str(x) + " " + str(y))
                    break
                else :
                    visited[x][y].append(beforea)
                a = graph[x][y][0]
            elif a == 'R':
                y+=int(graph[x][y][1])
                beforea = 'R'
                if beforea in visited[x][y]:
                    print(str(x) + " " + str(y))
                    break
                else :
                    visited[x][y].append(beforea)
                a = graph[x][y][0] 
            elif a == 'L':
                y-=int(graph[x][y][1])
                beforea = 'L'
                if beforea in visited[x][y]:
                    print(str(x) + " " + str(y))
                    break
                else :
                    visited[x][y].append(beforea)
                a = graph[x][y][0]
            elif a == 'B':
                x-=int(graph[x][y][1])
                beforea = 'B'
                if beforea in visited[x][y]:
                    print(str(x) + " " + str(y))
                    break
                else :
                    visited[x][y].append(beforea)
                a = graph[x][y][0]
        elif beforea == 'R':
            if a == 'F':
                y+=int(graph[x][y][1])
                beforea = 'R'
                if beforea in visited[x][y]:
                    print(str(x) + " " + str(y))
                    break
                else :
                    visited[x][y].append(beforea)
                a = graph[x][y][0]
            elif a == 'R':
                x-=int(graph[x][y][1])
                beforea = 'B'
                if beforea in visited[x][y]:
                    print(str(x) + " " + str(y))
                    break
                else :
                    visited[x][y].append(beforea)
                a = graph[x][y][0] 
            elif a == 'L':
                x+=int(graph[x][y][1])
                beforea = 'F'
                if beforea in visited[x][y]:
                    print(str(x) + " " + str(y))
                    break
                else :
                    visited[x][y].append(beforea)
                a = graph[x][y][0]
            elif a == 'B':
                y-=int(graph[x][y][1])
                beforea = 'L'
                if beforea in visited[x][y]:
                    print(str(x) + " " + str(y))
                    break
                else :
                    visited[x][y].append(beforea)
                a = graph[x][y][0]
        elif beforea == 'L':
            if a == 'F':
                y-=int(graph[x][y][1])
                beforea = 'L'
                if beforea in visited[x][y]:
                    print(str(x) + " " + str(y))
                    break
                else :
                    visited[x][y].append(beforea)
                a = graph[x][y][0]
            elif a == 'R':
                x+=int(graph[x][y][1])
                beforea = 'F'
                if beforea in visited[x][y]:
                    print(str(x) + " " + str(y))
                    break
                else :
                    visited[x][y].append(beforea)
                a = graph[x][y][0] 
            elif a == 'L':
                x-=int(graph[x][y][1])
                beforea = 'B'
                if beforea in visited[x][y]:
                    print(str(x) + " " + str(y))
                    break
                else :
                    visited[x][y].append(beforea)
                a = graph[x][y][0]
            elif a == 'B':
                y+=int(graph[x][y][1])
                beforea = 'R'
                if beforea in visited[x][y]:
                    print(str(x) + " " + str(y))
                    break
                else :
                    visited[x][y].append(beforea)
                a = graph[x][y][0]
        elif beforea == 'B':
            if a == 'F':
                x-=int(graph[x][y][1])
                beforea = 'B'
                if beforea in visited[x][y]:
                    print(str(x) + " " + str(y))
                    break
                else :
                    visited[x][y].append(beforea)
                a = graph[x][y][0]
            elif a == 'R':
                y-= int(graph[x][y][1])
                beforea = 'L'
                if beforea in visited[x][y]:
                    print(str(x) + " " + str(y))
                    break
                else :
                    visited[x][y].append(beforea)
                a = graph[x][y][0] 
            elif a == 'L':
                y+=int(graph[x][y][1])
                beforea = 'R'
                if beforea in visited[x][y]:
                    print(str(x) + " " + str(y))
                    break
                else :
                    visited[x][y].append(beforea)
                a = graph[x][y][0]
            elif a == 'B':
                x+=int(graph[x][y][1])
                beforea = 'F'
                if beforea in visited[x][y]:
                    print(str(x) + " " + str(y))
                    break
                else :
                    visited[x][y].append(beforea)
                a = graph[x][y][0]
        
                
