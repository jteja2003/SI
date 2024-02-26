
"""Example
Input
2
3
5 15 3
2
70 100
Output
23
170"""


for i in range(int(input())):
    s=int(input())
    l=list(map(int,input().split()))
    print(sum(l))