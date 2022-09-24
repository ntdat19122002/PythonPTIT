def check(n):
    for i in range(len(n)):
        if (n[i] != '4' and n[i] != '7'):
            return False
    return True

T = int( input() )
for t in range(T):
    n = input()
    if(check(n)):
        print('YES')
    else:
        print('NO')