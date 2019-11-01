# Given 2 lists a and b. Each element is a pair of integers 
# where the first integer represents the unique id 
# and the second integer represents a value. 
# Your task is to find an element from a and an element 
# form b such that the sum of their values is less or equal to
# target and as close to target as possible. Return a list of
# ids of selected elements. If no pair is possible, return an empty list.

# a = [[1, 3], [2, 5], [3, 7], [4, 10]]
# b = [[1, 2], [2, 3], [3, 4], [4, 5]]
# target = 10

# Output: [[2,4], [3,2]]

# Input:
# a = [[1, 8], [2, 15], [3, 9]]
# b = [[1, 8], [2, 11], [3, 12]]
# target = 20
#
# Output: [[1, 3], [3, 2]]

def optimalUtilization(a, b):
    result = []

    if a == [] or b == []:
        return result
