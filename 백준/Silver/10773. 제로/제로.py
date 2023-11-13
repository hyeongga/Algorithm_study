count = int(input())
nums = []

for i in range(count):
    a = int(input())
    if(a==0):
        nums.pop()
    else:
        nums.append(a)
print(sum(nums))