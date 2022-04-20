#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start

from functools import reduce
import operator


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # #! first method:
        # #? using hash sets
        # #? multiply all single elements by 2 and then subtract all elements
        # return sum(set(nums)) * 2 - sum(nums)
        # #! second method:
        # #? using bit manipulation
        # #? using the XOR operator where:
        # #? n ^ n = 0 || n ^ 0 = n
        # #? n ^ m ^ m = n ^ 0 = n
        # single = 0
        # for i in nums:
        #     single ^= i
        # return single
        #! third method:
        #? same thing as second method but using reduce()
        #? we can use operator.xor or lambda x, y: x ^ y
        return reduce(operator.xor, nums, 0)
# @lc code=end
