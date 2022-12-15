t = int(input())
for _ in range(t):
    n, m = map(int, input().split())  # 게시판에 전시 가능한 작품 수, 학생 추천 수
    good = list(map(int, input().split()))  # 1부터 100 사이의 작품 번호
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
            # print(f"추가 : {i}")
        else:
            old = -1
            low_good = 10000
            for j in number:
                # 오래된 순서가 나가므로 추천 수 같은 건 무시
                if board[j] < low_good:
                    old = j
                    low_good = board[j]
            board[old] = 0
            board[i] = 1
            number.remove(old)
            number.append(i)
            # print(f"제거 : {old}, 추가 : {i}")

    number.sort()
    for i in number:
        print(i, end=" ")
    print()