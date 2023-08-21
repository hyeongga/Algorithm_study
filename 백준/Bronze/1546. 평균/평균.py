a = int(input())
b =[0 for _ in range(a)]
b[:a] = map(int,input().split())
sum = 0
for i in range (a):
    sum += b[i]
print(sum/max(b)*100/a)