t = int(input())

for i in range(t):
    n = int(input())
    m = int(input())
    rec = list(map(int, input().split()))
    dic = {}
    ans = []
    before = 2
    idx = 0
    for i in range(m):
        dic[rec[i]] = 0
    for i in range(m):
        if len(ans) < n :
            if rec[i] not in ans:
                ans.append(rec[i])
            dic[rec[i]] +=1
        else:
            if rec[i] in ans :
                dic[rec[i]] +=1
            else:
                dic[rec[i]] +=1
                if dic[rec[i]] > before and i!=idx:
                    dic[ans[idx]] =0
                    del ans[idx]
                    ans.append(rec[i])
        for i in range(len(ans)):
            print(before, dic[ans[i]])
            if before > dic[ans[i]]  :
                before = dic[ans[i]]
                idx = i
        print(ans)
    ans.sort()
    for i in range(len(ans)):
        print(ans[i], end = ' ')
    print("")