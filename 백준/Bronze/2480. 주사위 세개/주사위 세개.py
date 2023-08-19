first, second, third = map(int,input().split())

if first == second == third:
    print (10000+first*1000)
elif first == second or first == third:
    print (1000+first*100)
elif second == third:
    print (1000+second*100)
else:
    print(max(first, second, third)*100)