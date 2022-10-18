for t in range(int(input())):
    n = input()
    chu = n[0]
    so=1
    for i in range(1,len(n)):
        if n[i]==n[i-1]:
            so+=1
        else:
            print(str(so)+chu,end='')
            chu=n[i]
            so=1
        if i==len(n)-1:
            print(str(so) + chu, end='')
    print()