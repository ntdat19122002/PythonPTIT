T = int(input())
for t in range(T):
    n = input()
    if(n[0]==n[len(n)-2] and n[1]==n[len(n)-1]):
        print('YES')
    else:
        print('NO')