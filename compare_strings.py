import unittest

def findMinCount(s):
    if len(s) <= 1:
        return len(s)
    minChar = min(s)
    count = 0
    for char in s:
        if char == minChar:
            count += 1
    return count

def compareStrings(s1, s2):
    arr1 = s1.split(" ")
    arr2 = s2.split(" ")
    if len(arr1) <= len(arr2):
        shorter, longer = arr1, arr2
    else:
        shorter, longer = arr2, arr1
    results = []
    for i in shorter:
        count = 0
        for j in longer:
            if findMinCount(j) < findMinCount(i):
                count += 1
        results.append(count)
    return results

assert compareStrings("abcd aabc bd", "aaa aa") == [3,2], "Should be [3,2]"
assert compareStrings("abcd aabc bd", "") == [3,3], "Should be [3,3]"