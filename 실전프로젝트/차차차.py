t = int(input())

for k in range(t):
    length = int(input())
    graph = []
    dp=[[0]*5 for i in range(length+1)]
    dp[0] = [-100, -100, 0, -100, -100]
    for i in range(length):
        graph.append(list(map(int,input().split())))
    graph.append([0, 0, 0, 0, 0])
    graph.reverse()
    #print(graph)
    for i in range(1,length+1):
        #print(i)
        for j in range(5):
            if(graph[i][j] ==1):
                dp[i][j] = -100
                continue
            dp[i][j] = dp[i-1][j]
            if(j>0):
                dp[i][j] = max(dp[i-1][j-1], dp[i][j])
            if(j<4):
                dp[i][j] = max(dp[i-1][j+1], dp[i][j])
            if(j>0):
                if( graph[i][j-1]==1):
                    dp[i][j] +=1
            if(j<4) :
                if(graph[i][j+1]==1):
                    dp[i][j] +=1
            if(graph[i][j]>1):
                dp[i][j] += graph[i][j]
    answer = 0
    for i in range(5):
        answer = max(dp[length][i], answer)
        #print(dp[length][i])
    print(answer)