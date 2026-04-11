class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet_str = ""

        for char in s:
            alphabet_str += char if char.isalnum() else ""
        
        print(alphabet_str)
        alphabet_str = alphabet_str.lower()
        str_reversed = "".join(reversed(alphabet_str))

        return alphabet_str == str_reversed

        