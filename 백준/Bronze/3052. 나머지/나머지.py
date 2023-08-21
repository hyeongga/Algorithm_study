import sys
b = []
for _ in range (10):
    b.append(int(sys.stdin.readline())%42)
print (len(set(b)))