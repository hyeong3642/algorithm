t= int(input())

for i in range(t):
    n, m = map(int, input().split())
    password = str(input())
    imaginary = str(input())
    ans = 0
    if password in imaginary :
        ans = 1
    print(ans)
