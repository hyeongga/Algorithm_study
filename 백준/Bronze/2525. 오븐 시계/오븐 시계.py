hour,minute = map(int,input().split())
time = int(input())
change =  minute + time
if (change < 60) :
    print(hour, change)
else:
    minute = change % 60
    hour += change//60
    if hour > 23:
        hour -= 24
    print(hour, minute)