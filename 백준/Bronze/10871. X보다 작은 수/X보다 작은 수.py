N,X = map(int,input().split())
A = list(map(int, input().split()))
count = []
for A in A:
    if A<X:
        print(A)