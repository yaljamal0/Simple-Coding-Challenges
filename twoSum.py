# LeetCode class method
#class Solution:
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
#       if not 2 <= len(nums) <= 10 ** 4\
#       or not -10 ** 9 <= target <= 10 ** 9:
#            return
#        for i in range(len(nums)):
#            for j in range(len(nums)):
#                if not -10 ** 9 <= nums[i] <= 10 ** 9:
#                    return
#                if nums[i] + nums[j] == target and i != j:
#                    return [i, j]
#

# Normal function definition
def twoSum(nums, target):
    if not 2 <= len(nums) <= 10 ** 4\
    or not -10 ** 9 <= target <= 10 ** 9:
        return
    for i in range(len(nums)):
        for j in range(len(nums)):
            if not -10 ** 9 <= nums[i] <= 10 ** 9:
                return
            if nums[i] + nums[j] == target and i != j:
                return [i, j]

# Test
nums = [3, 7, 4]
target = 7
print(twoSum(nums, target))
