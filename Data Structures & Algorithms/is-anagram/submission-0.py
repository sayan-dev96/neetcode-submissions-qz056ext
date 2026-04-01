class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=s.lower()
        t=t.lower()
        # sorted() function converts string into a sorted list of characters
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))

        return sorted_s == sorted_t