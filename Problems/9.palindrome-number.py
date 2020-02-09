#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            temp = 0
            xCopy = x
            while xCopy > 0:
                temp = (temp * 10) + (xCopy % 10)
                xCopy = xCopy // 10

            if x == temp:
                return True

        return False
        
# @lc code=end

