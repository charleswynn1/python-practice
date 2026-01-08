# Given an integer array nums, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
# Note: You must do this in-place without making a copy of the array.

def move(nums):
    if not 0 in nums:
        return nums
    write = 0
    for index, num in enumerate(nums):
        if nums[index] != 0:
            nums[write] = nums[index]
            write+=1
    for i in range(write,len(nums)):
        nums[i] = 0

    return nums

a = [0,1,0,3,12]
print(move(a))