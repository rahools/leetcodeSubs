#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        dupp = 0
        idx = 0
        # While cause cant back loop in for
        while (len(nums) - dupp) > idx:
            # checking 2nd time increases speed, WHAT? Hmmmm
            if nums[idx] == val and (len(nums) - dupp) > idx:
                for j in range(idx, len(nums) - 1 - dupp):
                    # Swap with space saving
                    nums[j] = nums[j] - nums[j + 1]
                    nums[j + 1] = nums[j + 1] + nums[j]
                    nums[j] = nums[j + 1] - nums[j]

                # Inc dupplicates, Dec idx to back loop
                dupp += 1
                idx -= 1
            idx += 1

        return len(nums) - dupp
        
# @lc code=end

