class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        for chars in zip(*strs):
            if len(set(chars))== 1:
                lcp +=chars[0]
            else:
                break
        return lcp