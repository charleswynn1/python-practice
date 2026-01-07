def highfreq(nums):
    if nums == []:
        return None
    
    fcounter = {}
    for num in nums:
        fcounter[num] = fcounter.get(num, 0) +1
    
    hf = max(fcounter.values())
    keys = []

    for k, v in fcounter.items():
        if v == hf:
            keys.append(k)
    for n in nums:
        if n in keys:
            return n
    return hf

a = [1,2,3,3]
print(highfreq(a))