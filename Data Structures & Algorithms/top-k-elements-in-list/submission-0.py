class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countChars = defaultdict(int)

        for num in nums:
            if num not in countChars:
                countChars[num] = 1
            else:
                countChars[num] += 1
        

        sorted_chars = dict(sorted(countChars.items(), key = lambda item: item[1], reverse=True))
        
        result = []
        counter = 0
        sorted_keys = list(sorted_chars.keys())
        for num in sorted_keys:
            result.append(int(num))
            counter += 1
            if counter == k:
                return result

