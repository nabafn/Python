x = int(input())
ans = x%5
ans1 = ans%4
ans2 = ans1%3
ans3 = ans2%2
ans4 = ans3%1
print(int(x/5) + int(ans/4) + int(ans1/3) + int(ans2/2) + int(ans3/1))