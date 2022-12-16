t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    rec = list(map(int, input().split()))
    board = {}
    ans = []
    count = 0

    for i in range(1, 101):
        board[i] = 0
    for i in rec:
        if board[i]!= 0:
            board[i] +=1
        elif count < n:
            board[i] +=1
            count +=1
            ans.append(i)
        else :
            old = -1
            oldrec = 10000
            for j in ans:
                if board[j]<oldrec:
                    old = j
                    oldrec = board[j]
            board[old] =0
            board[i] =1
            ans.remove(old)
            ans.append(i)
            
    #print(ans)
    ans.sort()
    for i in ans:
        print(i, end =' ')
    print(' ')
