t = int(input())
for _ in range(t):
    n, m = map(int, input().split()) 
    good = list(map(int, input().split()))  
    board = {}
    number = []
    count = 0
    for i in range(1, 101):
        board[i] = 0
    for i in good:
        if board[i] != 0:
            board[i] = board[i] + 1
        elif count < n:
            board[i] = 1
            number.append(i)
            count += 1
        else:
            old = -1
            low_good = 10000
            for j in number:
                if board[j] < low_good:
                    old = j
                    low_good = board[j]
            board[old] = 0
            board[i] = 1
            number.remove(old)
            number.append(i)

    number.sort()
    for i in number:
        print(i, end=" ")
    print()

