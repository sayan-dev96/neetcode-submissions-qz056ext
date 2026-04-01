class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_obj = {}
        t_obj = {}
        for i in s:
            if i in s_obj:
                s_obj[i] += 1
            else:
                s_obj[i] = 1
        for j in t:
            if j in t_obj:
                t_obj[j] += 1
            else:
                t_obj[j] = 1
        return s_obj == t_obj