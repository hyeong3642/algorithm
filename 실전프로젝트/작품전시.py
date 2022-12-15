t = int(input())

for i in range(t):
    n,m = map(int, input().split())
    rec = list(map(int, input().split()))
    dic = {}
    ans = []
    idx = 0
    for i in range(101):
        dic[i] = 0
    for i in rec:
        if dic[i] != 0 :
            dic[i] +=1
        elif idx < n :
            dic[i] =1
            ans.append(i)
            idx +=1
        else :
            old = -1
            recommend = 10000
            for j in ans:
                if dic[j] < recommend:
                    old = j
                    recommend = dic[j]
            dic[old] = 0
            dic[i] = 1
            ans.remove(old)
            ans.append(i)
    ans.sort()
    for i in range(len(ans)):
        print(ans[i], end = ' ')
    print("")