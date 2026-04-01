class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {} # value -> index
        for index, num in enumerate(nums):
            difference = target - num
            if difference in nums_map:
                return [nums_map[difference], index]
            nums_map[num] = index

