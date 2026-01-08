# Given a sorted array of integers numbers and an integer target,
# find two numbers in the array that add up to the target.
# Return the indices of these two numbers (using 1-based indexing, not 0-based).
# You may assume that each input has exactly one solution, and you may not use
# the same element twice.

# Example 1: Input: numbers = [2, 7, 11, 15], target = 9 Output: [1, 2]
# Explanation: 2 + 7 = 9, so return indices 1 and 2

def twosum(nums,target):
    target = target
    snums = sorted(nums)
    max = len(snums)-1

# My first walk through solving this issue
#    for index, value in enumerate(snums,1):
#        if value + snums[max] == target:
#            return [index,max+1]
#        if value + snums[max] > target:
#            max-=1
#        if value + snums[max] < target:
#            continue
#    return [index,max+1]

# My second walk through solving this issue
    left = 0
    right = len(snums) - 1
    while left < right:
        total = snums[left] + snums[right]
        if total == target:
            return [left +1, right +1]
        elif total > target:
            right -= 1
        else:
            left +=1 
    return (left+1, right+1)


a = [2, 7, 11, 15]
targ = 9
print(twosum(a,targ))