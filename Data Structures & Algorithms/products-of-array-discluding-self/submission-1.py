class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [0] * len(nums)

        for i in range(len(nums)):
            tmp = nums.copy()
            x = tmp.pop(i)
            result[i] = math.prod(tmp)
            
        return result