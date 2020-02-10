#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) > 0:
            ans = 1
            temp = nums[0]
            for i in nums:
                if i != temp:
                    nums[ans] = i
                    ans += 1
                    temp = i

            return ans
            
        return None

# @lc code=end

