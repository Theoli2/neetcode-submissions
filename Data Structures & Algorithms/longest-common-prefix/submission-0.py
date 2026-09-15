class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            for elem in strs:
                if shortest[i] != elem[i]:
                    return lcp
            lcp += shortest[i]
        return lcp