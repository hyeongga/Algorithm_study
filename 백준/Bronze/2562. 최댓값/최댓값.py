import sys
list =[]
for _ in range(9):
    list.append(int(sys.stdin.readline().rstrip()))
for i in range(9):
    if list[i] == max(list):
        print(f"{max(list)}\n{i+1}")
        break
