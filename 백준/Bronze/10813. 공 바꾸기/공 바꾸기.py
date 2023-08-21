import sys
N,M = map(int, sys.stdin.readline().split())
a = [i+1 for i in range (N)]
for _ in range (M):
    i,j=map(int,sys.stdin.readline().split())
    a[i-1],a[j-1] = a[j-1],a[i-1]
for i in range(N):
    print (a[i])