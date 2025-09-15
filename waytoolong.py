n = int(input())
i = 1
while i<=n:
    
    x = input()
    if len(x)<11:
        print(x)
    else:
        print(x[0]+str(len(x)-2)+x[len(x)-1])
    i +=1
    
    
