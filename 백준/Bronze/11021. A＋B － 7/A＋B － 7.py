import sys

T = int(sys.stdin.readline())
for i in range(T):
    a,b = map(int, sys.stdin.readline().split())
    print(f"Case #{i+1}: {a+b}")