c = int(input())
for i in range(c):
    stair = list(map(int, input().split()))
    a = stair[0]
    b = stair[1:]
    cur = 0
    last = a
    tmp = 0
    while (cur<last) :
        if cur+2 not in b :
            cur+=2
            tmp +=1
        else :
            cur +=1
            tmp+=1
    print(tmp)
