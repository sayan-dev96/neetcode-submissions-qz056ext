class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp_res = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            if tmp_res:
                if sorted_s in tmp_res:
                    tmp_res[sorted_s].append(s)
                else:
                   tmp_res[sorted_s] = []
                   tmp_res[sorted_s].append(s) 
            else:
                tmp_res[sorted_s] = []
                tmp_res[sorted_s].append(s)
        
        return list(tmp_res.values())