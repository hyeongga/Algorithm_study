people = int(input())
array=list(map(int,input().split()))
array.sort(reverse=False)

times =0
totalTime = 0

for time in array:
    times += time
    totalTime += times
    
print(totalTime)