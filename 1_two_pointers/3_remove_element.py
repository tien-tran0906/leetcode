"""
Given an integer array `nums`, an int `val`
Remove all occurrences of val in nums, in-place.
Return the len of the final list

"""

nums = [0,1,2,2,3,0,4,2]
val = 2
# [0,1,3,0,4,2,2]
# basically swapping all the `val` towards the end
# return the index before the `val` starts