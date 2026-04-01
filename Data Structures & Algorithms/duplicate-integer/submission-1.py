class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = 1
        for k in nums:
            nums2 = nums[counter:len(nums):1]
            for j in nums2:
                if k == j:
                    return True
            counter += 1
        return False