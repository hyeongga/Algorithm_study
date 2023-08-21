n, m = map(int, input().split())
data = [0] * n

for _ in range(m) :
  i, j, k = map(int, input().split())
  for i in range(i, j + 1) :
    data[i-1] = k

for i in range(n) :
  print(data[i], end=' ')