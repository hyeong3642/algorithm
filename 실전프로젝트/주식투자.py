t = int(input())

for i in range(t):
    length = int(input())
    a = list(map(int, input().split()))
    ans = 0
    max = 0
    for i in range(length-1, -1, -1):
        if(max<a[i]):
            max = a[i]
        else :
            ans += max-a[i]
    print(ans)