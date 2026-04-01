class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_obj = {}
        t_obj = {}
        for i in range(len(s)):
            s_obj[s[i]] = 1 + s_obj.get(s[i], 0)
            t_obj[t[i]] = 1 + t_obj.get(t[i], 0)
        return s_obj == t_obj