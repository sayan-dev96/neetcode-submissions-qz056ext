class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProductArr = [1] * len(nums)
        rightProductArr = [1] * len(nums)

        leftProduct = 1
        rightProduct = 1
        for i in range(len(nums)):
            if i > 0:
                leftProduct *= nums[i-1]
            leftProductArr[i] = leftProduct
        
        for i in range(len(nums), 0, -1):
            if i < len(nums):
                rightProduct *= nums[i]
            rightProductArr[i-1] = rightProduct

        productArr = [0] * len(nums)

        for i in range(len(nums)):
            productArr[i] = leftProductArr[i] * rightProductArr[i]
        
        # print(leftProductArr)
        # print(rightProductArr)
        # print(productArr)
        return productArr
