"""
Input: "ab-cd-ef" 
Output: "fe-dc-ba"

fe-dc-ba

Input: "abcd-EF-ga"
Output: "agFE-dc-ba"

ag-FE-dcba
"""

def customReverse(s):
    strList = list(s)
    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalpha():
            left += 1
        elif not s[right].isalpha():
            right -= 1
        else:
            strList[left], strList[right] = strList[right], strList[left]
            left += 1
            right -= 1

    return "".join(strList)

print(customReverse("abcd-EF-ga"))
