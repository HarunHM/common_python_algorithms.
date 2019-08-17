import random
from itertools import groupby

nums = []

for i in range(10):
    x = random.randint(0,10)
    nums.append(x)

def sort(nums): 
    for i in range(len(nums)-1, 0, -1):
        for x in range(i):
            if nums[x] > nums[x+1]:
                temp = nums[x]
                nums[x] = nums[x+1]
                nums[x+1] = temp   
                
print(nums)

sort(nums)
nums = [el for el, _ in groupby(nums)]