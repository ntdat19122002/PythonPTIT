def chan(n):
    for i in range(len(n)):
        if n[i]=='1' or n[i]=='3' or n[i]=='5' or n[i]=='7' or n[i]=='9':
            return False
    return True
def tn(n):
    for i in range(int(len(n)/2)+1):
        if(n[i] != n[len(n)-i-1]):
            return False
    return True
def le(n):
    return len(n)%2==0
for t in range(int(input())):
    n = input()
    a = int(n)
    for i in range(22,a):
        if le(str(i)) and tn(str(i) and chan(str(i)) ):
            print(i,end=' ')
    print()
