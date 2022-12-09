t = int(input())

for i in range(t):
    n = int(input())
    tree = list(map(int, input().split()))
    tree.insert(0, 0)


    def inorder(i):
        if i*2 <= n:
            inorder(i*2)
        print(tree[i], end= ' ')
        if i*2+1 <= n:
            inorder(i*2+1)
        
    def preorder(i):
        print(tree[i] , end =' ') 
        if i*2 <= n:
            preorder(i*2)
        if i*2+1 <= n:
            preorder(i*2+1)

    def postorder(i):
        if i*2 <= n:
            postorder(i*2)
        if i*2+1 <= n:
            postorder(i*2+1)
        print(tree[i], end= ' ')
 
    inorder(1)
    print()
    preorder(1)
    print()
    postorder(1)
    print()