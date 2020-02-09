#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) != 0:
            strLen = min([len(i) for i in strs])
        else:
            strLen = 0
        temp = ''
        for idx in range(strLen):
            if len(set([i[idx] for i in strs])) == 1:
                temp = temp + strs[0][idx]
            else:
                return temp
        return temp

# @lc code=end

