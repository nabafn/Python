k, n, w = map(int, input().split())
l = (k*w*(w+1))/2 - n
if int(l) > 0:
    print(int(l))
else:
    print(0)