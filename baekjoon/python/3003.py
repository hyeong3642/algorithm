chess = [1, 1, 2, 2, 2, 8]
a = list(input().split())
b=[]
for i in range(len(chess)):
    b.append(chess[i]-int(a[i]))
c = ''
for i in range(len(b)):
    c += str(b[i]) + ' '

print(c)