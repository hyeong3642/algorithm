t = int(input())

for i in range(t):
    length = int(input())
    a = list(map(str, input().split()))
    post = []
    stack = []
    for s in a:
        if s.isdecimal():
            post.append(s)
        else:
            if s == '(':
                stack.append(s)
            elif s == '+' or s == '-':
                while stack and stack[-1] != '(':
                    post.append(stack.pop())
                stack.append(s)
            elif s == '*' :
                while stack and stack[-1] == '*' :
                    post.append(stack.pop())
                stack.append(s)
            elif s == ')':
                while stack and stack[-1] != '(':
                    post.append(stack.pop())    
                stack.pop()
    while stack :
        post.append(stack.pop())
    stack2 = []
    for i in post :
        if i.isdecimal():
            stack2.append(i)
        else :
            num2 = int(stack2.pop())
            num1 = int(stack2.pop())
            if i == '+':
                stack2.append(num1+num2)
            if i == '-':
                stack2.append(num1-num2)
            if i == '*':
                stack2.append(num1*num2)
    print(stack2[0])





   