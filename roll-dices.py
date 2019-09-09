import unittest

def rollDices(arr):
    d = {}
    uniq = set(arr)
    uniq_len = len(uniq)
    pairs = 0
    for num1 in uniq:
        for num2 in uniq:
            if num1 != num2 and num1 + num2 == 7:
                pairs += 1
    if pairs == 0:
        return uniq_len - 1
    if len(uniq) > 0:
        return len(arr) - 1
    elif len(uniq) == 0:
        return len(arr)

assert rollDices([1,2,3]) == 2, "[1,2,3] should return 2"
assert rollDices([1,6,2,3]) == 3, "[1,6,2,3] should return 3"
assert rollDices([1,1,6]) == 2, "[1,1,6] should return 2"
assert rollDices([1,2,5,6]) == 4, "[1,2,5,6] should return 4"
assert rollDices([1,2,5,6,3]) == 4, "[1,2,5,6,3] should return 4"
assert rollDices([1,6,1,6,2,5]) == 6, "[1,6,1,6,2,5] should return 6"
