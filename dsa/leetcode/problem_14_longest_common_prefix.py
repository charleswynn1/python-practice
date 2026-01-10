"""
Longest Common Prefix

Problem
Find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string.

Approach
- Find length of shortest string (prefix can't be longer than this)
- Compare each character position across all strings
- Use first string's character as reference at each position
- Stop at first mismatch
"""
def lcp(s):        
    lindex = 0
    result = ""
    while lindex < len(min(s, key=len)):
        reference = s[0][lindex]
        for words in s:
            if words[lindex] != reference:
                return result
        result+=reference
        lindex+=1
    return result

s = ["flower","flow","flight"]
print(lcp(s))