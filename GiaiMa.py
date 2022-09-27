for t in range(int(input())):
    n = input()
    for i in range(0,len(n),2):
        for j in range(int(n[i+1])):
            print(n[i],end='')
    print()