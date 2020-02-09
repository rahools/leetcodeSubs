#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                temp.append(i)
            else:
                if len(temp) > 0:
                    if i == ')' and temp[-1] == '(':
                        temp.pop()
                    elif i == '}' and temp[-1] == '{':
                        temp.pop()
                    elif i == ']' and temp[-1] == '[':
                        temp.pop()
                    else:
                        return False
                else:
                    return False             

        if len(temp) == 0:
            return True
        return False


# @lc code=end

