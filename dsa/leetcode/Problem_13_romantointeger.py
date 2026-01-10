"""
Charles Wynn
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII,
which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
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