class Solution:

    def encode(self, strs: List[str]) -> str:
        return "|&|".join(strs) if strs not in [[]] else "-"

    def decode(self, s: str) -> List[str]:
        print(s)
        return s.split("|&|") if s not in ["-"] else []
