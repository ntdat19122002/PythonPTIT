import math
def tong(a):
    sum = 0
    while a>0:
        sum+=int(a%10)
        a = int(a/10)
    return sum
def nt(a):
    if(a<2):
        return False
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            return False
    return True
for t in range(int(input())):
    a,b = [int(i) for i in input().split()]
    if(nt(tong(math.gcd(a,b)))):
        print('YES')
    else:
        print('NO')

