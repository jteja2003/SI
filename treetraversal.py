class TreeNode:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data

def insert(root,data):
    if root==None:
        return TreeNode(data)
    if data<root.data:
        root.left=insert(root.left,data)
    else:
        root.right=insert(root.right,data)
    return root

def inorder(root):
    if root==None:
        return None
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
def postorder(root):
    if root==None:
        return None
    if root:
        print(root.data,end=" ")
        postorder(root.left)
        postorder(root.right)

def preorder(root):
    if root==None:
        return None
    if root:
        preorder(root.left)
        preorder(root.right)
        print(root.data,end=" ")

for i in range(int(input())):
    le=int(input())
    l=list(map(int,input().split()))
    root=None
    for i in l:
        root=insert(root,i)
    print("inorder:")
    inorder(root)
    print()
    print("postorder:")
    postorder(root)
    print()
    print("preorder:")
    preorder(root)
    print()
    print()




