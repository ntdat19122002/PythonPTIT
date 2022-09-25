s=input()
up=0
low=0
for i in range(len(s)):
    if(s[i].isupper()):
        up+=1
    else:
        low+=1
if(up>low):
    print(s.upper())
else:
    print(s.lower())