# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10


def countBits(nums):
    ans=[]
    for i in range(nums+1):
        ans.append(hammingWeight(i))
    return ans
def hammingWeight(n):
    res=0
    while n!=0:
        res+=n&1
        n=n>>1
    return res

print(countBits(2))