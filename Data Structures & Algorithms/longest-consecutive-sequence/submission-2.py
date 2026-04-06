class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longestSubSequenceLen = 0
        setNums = set(nums)
        sorted_array = sorted(list(setNums))
        tmpSequence = 1
        # if sorted_array == [0]:
        #     return tmpSequence

        for i in range(len(sorted_array)):
            currentElement = sorted_array[i]
            nextElement = currentElement + 1
            for j in range(i+1, len(sorted_array)):
                if sorted_array[j] == nextElement:
                    tmpSequence += 1
                    nextElement += 1
                else:
                    break
            if tmpSequence > longestSubSequenceLen:
                longestSubSequenceLen = tmpSequence
            tmpSequence = 1
        
        return longestSubSequenceLen

