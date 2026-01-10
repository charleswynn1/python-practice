"""
LeetCode 13: Roman to Integer

Author: Charles Wynn

Approach:
- Handle subtractive Roman numeral pairs first (IV, IX, XL, XC, CD, CM)
- Remove them from the string
- Add remaining symbol values
"""
def romanToInt(s):
        result = []
        if "CM" in s:
            result.append(900)
            s = s.replace("CM","")
        if "CD" in s:
            result.append(400)
            s = s.replace("CD","")
        if "XC" in s:
            result.append(90)
            s = s.replace("XC","")
        if "XL" in s:
            result.append(40)
            s = s.replace("XL","")
        if "IX" in s:
            result.append(9)
            s = s.replace("IX","")
        if "IV" in s:
            result.append(4)
            s = s.replace("IV","")
        for i in s:
            if i == "I":
                result.append(1)
            if i == "V":
                result.append(5)
            if i == "X":
                result.append(10)
            if i == "L":
                result.append(50)
            if i == "C":
                result.append(100)
            if i == "D":
                result.append(500)
            if i == "M":
                result.append(1000)
        result = sum(result)
        return result

s = "MCMXCIV"
print(romanToInt(s))