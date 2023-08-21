N,M = map(int,input().split())
result =[0]*N

for _ in range(M):
    i,j,k = map(int,input().split())
    for i in range(i,j+1):
        result[i-1] = k
for i in range(N):  
    print (result[i],end=" ")