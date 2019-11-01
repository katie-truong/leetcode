"""
Given an array A that is a permutation of n numbers [1-n]. Find the number of subarrarys S that meets the following condition max(S) - min(S) = length(S) - 1.
Example 1:
Input: [4, 3, 1, 2, 5] -> [1, 2, 3, 4, 5]

[4, 3, 1, 2, 5]
 ^     ^

[1, 2, 3, 4, 5]
 ^     ^

Output: 10
Explanation:
subarrays that meets the condition are
[4]
[3]
[1]
[2]
[5]
[4 3]
[1 2]
[3 1 2]
[4 3 1 2]
[4 3 1 2 5]
There are 10 subarray that meets the condition, so the answer should be 10.
Is there a better than O(n^2) solution?
"""
import unittest

def findSubarrays(arr):
    if len(arr) <= 1:
        return len(arr)

    result = 0
    left = 0
    right = 0

    while left < len(arr):
        result += 1
        


    

assert findSubarrays([4,3,1,2,5]) == 10, "[4,3,1,2,5] should return 10"