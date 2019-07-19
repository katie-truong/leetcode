"""
You are given an array of characters arr that consists of sequences of characters separated by space characters. Each space-delimited sequence of characters defines a word.

Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.

Explain your solution and analyze its time and space complexities.

input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ]

"""

def reverse_words(arr):
    if " " not in arr:
      return arr
    # reverse all characters:
    n = len(arr)
    mirrorReverse(arr, 0, n-1)

    # reverse each word:
    wordStart = None
    for i in range (n):
        if (arr[i] == ' '):
            if (wordStart != None):
                mirrorReverse(arr, wordStart, i-1)
                wordStart = None
        elif (i == n - 1):
            if (wordStart != None):
                mirrorReverse(arr, wordStart, i)
        else:
            if (wordStart == None):
                wordStart = i

    return arr


# helper function - reverses the order of items in arr
# please note that this is language dependent:
# if are arrays sent by value, reversing should be done in place

def mirrorReverse(arr, left, end):
    while (start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1