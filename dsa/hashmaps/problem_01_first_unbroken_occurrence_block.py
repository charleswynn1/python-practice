# Problem 01: First Unbroken Occurrence Block
#
# Write a function that takes a sequence of integers and returns the first value
# whose appearances form one uninterrupted block.
#
# A value qualifies if:
# - It appears more than once
# - After its first appearance, all remaining appearances occur consecutively
#
# Return the first qualifying value from left to right.
# If no value qualifies, return None.
# Examples:
# [1, 2, 3, 3, 3] → 3
# [4, 4, 5, 4] → None
# [6, 7, 7, 7] → 7
# [1, 2, 1, 1] → None
# [] → None

def unbroken(nums):
    hash = {}
    for index, value in enumerate(nums): #looping through list of integers
        hash[value] = hash.get(value, {})
        hash[value][index] = hash[value].get(index, 0) +1
    for value in hash: #looping through hashmap indecies
        if len(hash[value]) > 1: #filerting for more than one occurance
           keys = []
           for x in hash[value]: #extracting the indexes to identify consecutive groupings
               keys.append(x)
               if len(keys) == len(hash[value]): #filtering for lists that match indecie count
                   increment = 0
                   keys = sorted(keys)
                   for i in range(1, len(keys)): #looping through indecies
                       if keys[i] - keys[i-1] != 1:
                           increment = 0
                           break
                       if keys[i] - keys[i-1] == 1:
                           increment+=1 #increasing count for consecutive indecies
                           if increment == len(keys)-1: #filter for 100% consective indecies
                               return(value) #return value
                                     
    return None

a = [1, 2, 3, 3, 3]
print(unbroken(a))