T = int(input())
for t in range(T):
    a,b,c = input().split()
    a,b,c = float(a),float(b),float(c)
    nam = 0
    while(a<c):
        nam+=1
        a+=a*b/100
    print(nam)