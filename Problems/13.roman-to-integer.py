#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        temp = 0
        for idx, i in enumerate(s):
            if i == 'M':
                temp += 1000

            elif i == 'D':
                temp += 500
            elif i == 'C':
                if idx + 1 < len(s) and (s[idx + 1] == 'M' or s[idx + 1] == 'D'):
                    temp -= 100
                else:
                    temp += 100

            elif i == 'L':
                temp += 50
            elif i == 'X':
                if idx + 1 < len(s) and (s[idx + 1] == 'C' or s[idx + 1] == 'L'):
                    temp -= 10
                else:
                    temp += 10

            elif i == 'V':
                temp += 5
            elif i == 'I':
                if idx + 1 < len(s) and (s[idx + 1] == 'X' or s[idx + 1] == 'V'):
                    temp -= 1
                else:
                    temp += 1
        
        return temp


        
# @lc code=end

