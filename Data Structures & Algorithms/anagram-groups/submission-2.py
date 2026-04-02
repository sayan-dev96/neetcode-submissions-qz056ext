class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        tmp_res = {}
        for s in strs:
            if tmp_res:
                if s not in tmp_res:
                    # Check anagram with keys of tmp_res
                    flag = False
                    for i in tmp_res:
                        flag = check_anagram(i, s)
                        if flag:
                            tmp_res[i].append(s)
                            break
                    if not flag:
                        tmp_res[s] = []
                        tmp_res[s].append(s)
                else:
                    tmp_res[s].append(s)
            else:
                tmp_res[s] = []
                tmp_res[s].append(s)
        
        result = []
        for v in tmp_res.values():
            result.append(v)
        
        return result

def check_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    if s1 == s2:
        return True

    s1_obj = {}
    s2_obj = {}
    for c in range(len(s1)):
        s1_obj[s1[c]] = 1 + s1_obj.get(s1[c], 0)
        s2_obj[s2[c]] = 1 + s2_obj.get(s2[c], 0)

    return s1_obj == s2_obj            

        