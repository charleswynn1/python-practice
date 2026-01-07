# Write a function that takes a list of integers and returns
# the length of the longest sequence of consecutive integers
# that can be formed from the list's elements.
#
# The integers in the list may appear in any order.
#
# For example, if the list contains [100, 4, 200, 1, 3, 2],
# the longest consecutive sequence is [1, 2, 3, 4], so return 4.

def longestv(nums):
    s = sorted(nums) #sort array 
    longest = 0
    current = 1
    for i in range(1, len(s)): #loop through array to get longest list of numbers
        if s[i] - s[i-1] == 0: #skip duplicates
             continue
        if s[i] - s[i-1] == 1: #check for consecutive integers
            current += 1
        if s[i] - s[i-1] != 1: #stop tracking current sequence if integers are not consecutive
            if current > longest: #check if current sequence is > the longest
                longest = current 
            current = 1
    if current > longest: #handle cases where all numbers are consecutive
            longest = current
    if s == []: #handle edge case empty array
        return 0
    return longest

a = [5]
print(longestv(a))