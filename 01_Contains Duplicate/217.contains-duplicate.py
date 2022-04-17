#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # #! first method:
        # #? count the number of appearances of each element
        # #? and check if any of them it is greater than 1
        # nums_count = {}
        # for num in nums:
        #     if num in nums_count:
        #         nums_count[num] += 1
        #     else:
        #         nums_count[num] = 1
        # #? check if any of the values is greater than 1
        # return any(value > 1 for value in nums_count.values())
        # #! second method:
        # #? go through the list one and add each new element to a hash
        # #? for each new element check if its twin is altready in the hash
        # unique = set()
        # for num in nums:
        #     if num in unique:
        #         return True
        #     else:
        #         unique.add(num)
        # return False
        #! third method:
        #? use python builtin set() ( only unique items )
        #? if there are only unique items then the length of the set is the same as the length of the list
        return len(nums) != len(set(nums))
# @lc code=end
