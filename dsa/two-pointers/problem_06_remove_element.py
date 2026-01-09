# Given an integer array nums and an integer val, remove all occurrences of val
# in nums in-place. The order of the elements may be changed.
# Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k.
# 
# To get accepted, you need to do the following:
# Change the array nums such that the first k elements of nums contain the
# elements which are not equal to val The remaining elements of nums are not
# important, as well as the size of nums
# Return k

def remove(nums, val):
    write = 0
    k = 0
    for search in range(len(nums)):
        if nums[search] != val:
            nums[write] = nums[search]
            write += 1

    return write

nums = [3,2,2,3]
val = 3
print(remove(nums, val))