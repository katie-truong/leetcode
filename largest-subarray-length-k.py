import unittest

def largest_subarray_length_k(arr, k):
    if len(arr) <= k:
        return arr

    for i in range(0, k):
        if compareArrays(arr, i, k):
            return arr[compareArrays(arr, i, k):compareArrays(arr, 0, k)+k]


def compareArrays(arr, start, k):
    maxStartingPoint = [float('-inf'), None]
    for i in range(start, len(arr)-k+1+start):
        if arr[i] > maxStartingPoint[0]:
            maxStartingPoint = [arr[i], i]
        elif arr[i] == maxStartingPoint[0]:
            return None
    return i

assert largest_subarray_length_k([1,2,3,4], 4) == [1,2,3,4], "Should be [1,2,3,4]"



