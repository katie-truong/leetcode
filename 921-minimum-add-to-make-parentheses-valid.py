"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.
"""

# Using a stack: time complexity: O(n), space complexity: O(n)
def minAddToMakeValid(self, S):
    if S == "":
        return 0
    total = 0
    d = []
    for char in S:
        if char == ")":
            if len(d) > 0:
                if d[-1] == "(":
                    d.pop()
            else:
                total += 1
        else:
            d.append(char)
    if len(d) == 0:
        return total
    else:
        return total + len(d)

# Using constant variables: time complexity: O(n), space complexity: O(1)
def minAddToMakeValid2(self, S):
    if S == "":
        return 0
    bal = 0
    total = 0
    for char in S:
        if char == ")":
            if bal > 0:
                bal -= 1
            else:
                total += 1
        else:
            bal += 1
    if bal == 0:
        return total
    else:
        return bal + total