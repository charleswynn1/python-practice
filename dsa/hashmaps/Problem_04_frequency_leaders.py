# Write a function that takes a list of integers and returns a new list
# containing only the integers that appear more frequently than all integers
# that come before them in the original list.
#
# For example, if the input is [1, 2, 1, 3, 2, 2, 4], the integer 1 appears
# twice (more than any element before it, since there are none), 2 appears
# three times (more than 1's two appearances), but 3 only appears once
# (less than 2's three), and 4 only appears once. So return [1, 2].

def frequency_leaders(nums):
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) +1

    keycheck = None
    result = []
    for index, key in enumerate(nums):
        if keycheck == None:
            result.append(key)
            keycheck = key
        if keycheck == key:
            continue
        if counter[key] > counter[keycheck]:
            result.append(key)
            keycheck = key
        #print(index,key, counter[key])
    return result
        #if counter[key] in counter > counter[key]:


a = []
print(frequency_leaders(a))