a, b = map(int, input().split())
i = 1
while True:
    if a*(3**i) - b*(2**i) > 0:
        print(i)
        break
    i += 1  