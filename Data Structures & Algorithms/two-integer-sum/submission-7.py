class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)-1):
            difference = target - nums[i]
            if difference in nums[i+1:]:
                print(difference)
                pos = nums.index(difference, (i+1), len(nums))
                return [i, pos]
        return []