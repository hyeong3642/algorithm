t = int(input())
for i in range(t):
    d = int(input())
    days = list(map(int, input().split()))
    days.reverse()
    ans = 0
    max = days[0]
    for i in range(1, len(days)):
        if days[i] > max:
            max = days[i]
        else :
            ans += max - days[i]
    print(ans)