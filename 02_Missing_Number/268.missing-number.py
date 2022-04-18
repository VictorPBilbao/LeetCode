#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # #! first method:
        # #? sort the array and create a range from 0 to len(nums) and check
        # #? what is the number missing
        # nums.sort()
        # for idx, num in enumerate(nums):
        #     if idx != num:
        #         return idx
        # return nums[-1] + 1
        #! second method:
        # #? same thing but using the next function nas list comprehension
        # #? (idx for idx, num in enumerate(nums) if idx != num)
        # #? next(iterator, default value)
        # nums.sort()
        # return next((idx for idx, num in enumerate(nums) if idx != num), nums[-1] + 1)
        #! third method:
        #? using math and sum of the array
        #? the sum of a sequence is n * (n + 1) / 2
        #? the predicted sum - the actual sum = missing number
        n = len(nums)
        return (n * (n + 1) // 2) - sum(nums)
# @lc code=end
