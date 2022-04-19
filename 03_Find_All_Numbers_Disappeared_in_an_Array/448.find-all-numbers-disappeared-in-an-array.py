#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # #! first method:
        # #? go through each number in the list and remove it from its hash
        # result = set(range(1, len(nums) + 1))
        # for num in nums:
        #     if num in result:
        #         result.remove(num)
        # return list(result)
        #! second method:
        #? using sets subtraction where:
        #? {1, 2, 3, 4} - {2, 3} = {1, 4}
        #? real_range - nums = result
        return list(set(range(1, len(nums) + 1)) - set(nums))
# @lc code=end
