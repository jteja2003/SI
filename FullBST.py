"""
Given an array of unique elements, construct a Binary Search Tree and check if it is a Full Binary Tree [FBT]. A FBT is one in which each node is either a leaf or possesses exactly 2 child nodes
Input Format
The first line of input contains T - the number of test cases. It is followed by 2T lines. The first line of each test case contains N - the number of nodes in the BST. The next line contains N unique integers - value of the nodes.
Output Format
For each test case, print "True" if the Binary Search Tree is an FBT, "False" otherwise, separated by a newline.
Constraints
1 <= T <= 1000
1 <= N <= 1000
0 <= ar[i] <= 10000
Example
Input
3
5
1 2 3 4 5
11
8 3 30 15 40 18 12 17 25 1 7
7
4 5 15 0 1 7 17
Output
False
True
False
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def insert(root,val):
    if root==None:
        return TreeNode(val)
    if val<root.val:
        root.left=insert(root.left,val)
    else:
        root.right=insert(root.right,val)
    return root
def F_bst(root):
    if root==None:
        return True
    if (root.right==None and root.left) or (root.left==None and root.right):
        return False
    return F_bst(root.right) and F_bst(root.left)
for i in range (int(input())):
    l=int(input())
    l=list(map(int,input().split()))
    root=None
    for i in l:
        root=insert(root,i)
    pi=F_bst(root)
    print(pi)