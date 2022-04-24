#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#


# @lc code=start
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # #! first method:
        # #? using a triple for loop to find the max subarray
        # #? this is O(n^3) time complexity
        # #? i for the initial pointer of the subarray
        # #? j for the final pointer of the subarray
        # #? third loop to calculate the sum of the subarray
        # max_sum = nums[0]
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         cur_sum = 0
        #         for k in range(i, j + 1):
        #             cur_sum += nums[k]
        #         if cur_sum > max_sum:
        #             max_sum = cur_sum
        # return max_sum
        # #! first method v2:
        # #? using python built-in function to find the max subarray
        # max_sum = nums[0]
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         cur_sum = sum(nums[k] for k in range(i, j + 1))
        #         max_sum = max(max_sum, cur_sum)
        # return max_sum
        #! second method:
        #? it doesn't make sense for the subarray to start with a negative number
        #? we can skip it
        max_sum = nums[0]
        cur_sum = 0
        
        for num in nums:
            cur_sum = max(cur_sum, 0)
            cur_sum += num
            max_sum = max(max_sum, cur_sum)
        return max_sum

# @lc code=end
