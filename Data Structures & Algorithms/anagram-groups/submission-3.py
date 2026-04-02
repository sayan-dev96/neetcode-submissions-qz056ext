class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp_res = {}

        for s in strs:
            sorted_s_list = sorted(s)
            sorted_s = "".join(sorted_s_list)
            if tmp_res:
                if sorted_s in tmp_res:
                    tmp_res[sorted_s].append(s)
                else:
                   tmp_res[sorted_s] = []
                   tmp_res[sorted_s].append(s) 
            else:
                tmp_res[sorted_s] = []
                tmp_res[sorted_s].append(s)
        
        result = []
        for v in tmp_res.values():
            result.append(v)
        
        return result