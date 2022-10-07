t = int(input())

for i in range(t):
    size, cvs = map(int,input().split())
    graph = [[0]* size for _ in range(size)]
    for j in range(cvs):
        n, m = map(int,(input().split()))
        graph[n][m] = 1
    ans = [[0]* size for _ in range(size)]
    for n in range(size):
        for m in range(size):
            if graph[n][m] == 1:
                for k in range(-3,4):
                    for l in range(-3,4):
                        if k == 0 and l == 0 :
                            continue
                        if 0<= n+k and (n+k <size) and 0<= m+l and (m+l <size):
                            if abs(k) + abs(l) <=3:
                                ans[n+k][m+l] +=2
                for k in range(-10,11):
                    for l in range(-10,11):
                        if k == 0 and l == 0 :
                            continue
                        if 0<= n+k and (n+k <size) and 0<= m+l and (m+l <size):
                            if (abs(k) + abs(l)) <=10:
                                ans[n+k][m+l] +=1
    for n in range(size):
        for m in range(size):
            if graph[n][m] == 1:
                ans[n][m] == 0
    max = 0
    tmpx = 0
    tmpy = 0
    for n in range(size):
        for m in range(size):
            if ans[n][m] > max:
                max = ans[n][m]
                tmpx = n
                tmpy = m
            if ans[n][m] == max:
                if n < tmpx :
                    tmpx = n
                if n == tmpx:
                    tmpy = min(tmpy, m)
    print(tmpx, tmpy, max)