# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Return the number of unique elements in nums.
#
# Important: You must modify the array in-place with O(1) extra memory.
# The first k elements of nums should hold the unique values, where k is the number you return.
def remove(nums):
    write = 0
    for read in range(1, len(nums)):
        if nums[read] == nums[write]:
            continue
        if nums[read] != nums[write]:
            write += 1
            nums[write] = nums[read]
            continue
    return write+1

nums = [0,0,1,1,1,2,2,3,3,4]
print (remove(nums))