
"""Input

4
2
1
5
10


Output

Case #1:
 *
**
Case #2:
*
Case #3:
    *
   **
  ***
 ****
*****
Case #4:
         *
        **
       ***
      ****
     *****
    ******
   *******
  ********
 *********
**********
"""




t=int(input())
for i in range(t):
    print("Case #"+str(i+1)+":")
    n=int(input())
    for i in range(n):
        for j in range(0,n-i-1):
            print(" ",end="")
        for j in range(n-i-1,n):
            print("*",end="")
        print()