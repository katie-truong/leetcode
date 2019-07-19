"""
Given a static-sized array of integers arr, move all zeroes in the array to the end of the array. You should preserve the relative order of items in the array.

We should implement a solution that is more efficient than a naive brute force.
"""
def moveZerosToEnd(arr):
  if len(arr) <= 1:
    return arr
  
  index = 0
  
  for i in range(len(arr)):
    if arr[i] != 0:
      arr[index] = arr[i]
      index += 1
    else:
      continue
      
  while index < len(arr):
    arr[index] = 0
    index += 1
    
  return arr
