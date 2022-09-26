a,k,n = [int(i) for i in input().split()]
check =True
for i in range(a+1,n):
    if(i%k==0):
        print(i,end=' ')
        check = False
if check:
    print(-1)