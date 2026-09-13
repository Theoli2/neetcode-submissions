class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        ans = ans + nums
        ans += nums
        return(ans)