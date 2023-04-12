N,K = map(int,input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.reverse()
count = 0

for coin in coins:
    count += K//coin
    K = K%coin
    
print(count)
