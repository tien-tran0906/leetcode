"""
Two Sum (Sorted)

Given a sorted array `nums`
Find two numbers that adds up to the `target`
Return their index

Constraint:
- Solution must use constant space
- Only 1 solution
- All array items are bigger/equal to 1
"""


"""
Thought
- Need to find two integers, and the two integers could be anywhere in the array
- Considering 2 points in the array
- Because the array is sorted, you need to consider that whenever the sum is bigger than the target, we don't need to go on anymore

https://youtu.be/cQ1Oz4ckceM?si=QGWe9rhp_fkHZC0E
"""


nums = [2,3,4,6,8,10]
target = 11  # return [1,4]