'''for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(n):
        p=i
        for j in range(i,n):
            if l[p]>l[j]:
                l[i],l[j]=l[j],l[i]
                print(i)


    print(l)'''
def selectionSort(ar,n):
    for i in range(n-1):
        maxi=0
        for j in range(1,n-i,1):
            if(ar[j]>ar[maxi]):
                maxi=j
        print(maxi, end=' ')
        ar[maxi], ar[n-1-i] = ar[n-1-i], ar[maxi]
    print()


k=int(input())
for i in range(k):
    n=int(input())
    ar=list(map(int, input().split()))[:n]
    selectionSort(ar,n)