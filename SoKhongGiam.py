def check(n):
    for i in range(len(n)-1):
        if int(n[i])>int(n[i+1]):
            return False
    return True
for t in range(int(input())):
    if(check(input())):
        print('YES')
    else:
        print('NO')