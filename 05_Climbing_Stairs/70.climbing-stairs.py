#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    
    cache = {1: 1, 2: 2, 3: 3}
    
    def climbStairs(self, n: int) -> int:
        # #! first method:
        # #? first do some test cases
        # #? 1 stair --> 1
        # #? 2 stairs --> 2
        # #? 3 stairs --> 3
        # #? 4 stairs --> 5
        # #? 5 stairs --> 8
        # #? we can see that the number of steps on each level
        # #? is equal to the sum of the 2 previous levels
        # #? we can use recursion to solve this problem but it will get very slow over time
        # #* first set the default stop case
        # if 0 <= n <= 3:
        #     return n
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        #! second method:
        #? using a cache to store previous results so
        #? we don't need to calculate the same result again
        if n not in self.cache:
            self.cache[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.cache[n]
# @lc code=end