# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
#tc=O(n)
#sc O(1)
# XOR
# x y  x^y
# 0 0   0
# 0 1   1
# 1 0   1
# 1 1   0

# xor on same numbers cancel out each other
def SingleNumber(nums):
    res=0
    for i in nums:
        res^=i
    return res

print(SingleNumber([2,3,3,2,1]))