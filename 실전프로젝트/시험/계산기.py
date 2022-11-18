t = int(input())
for i in range(t):
    length = int(input())
    a= input().split()
    d = []
    e = []
    prior = {'*':3, '+':2, '-':2, '(':1}

    for i in range(len(a)):
        if a[i].isdigit():
            d.append(a[i])
        elif a[i]=='(':
            e.append(a[i])
        elif a[i] == ')':
            while e[-1] != '(':
                d.append(e.pop())
            e.pop()
        else:
            while e and prior[a[i]] <= prior[e[-1]]:
                d.append(a[i])
            e.append(a[i])
    while len(e) != 0:
        d.append(e.pop())
    for i in range(len(d)):
        if d[i].isdigit():
            e.append(int(d[i]))
        else:
            b= e.pop()
            c = e.pop()
            if d[i] == '+':
                e.append(b+c)
            elif d[i] == '-':
                e.append(c-b)
            else:
                e.append(b*c)
    print(e[0])