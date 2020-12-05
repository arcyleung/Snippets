class Solution:
    def reverseString(self, s) -> None:
        self.swapIdx(0, len(s) -1, s)
        print(s)
        """
        Do not return anything, modify s in-place instead.
        """
    def swapIdx(self, lIdx, rIdx, s):
        if lIdx >= rIdx:
            return 
        tmp = s[lIdx]
        s[lIdx] = s[rIdx]
        s[rIdx] = tmp
        self.swapIdx(lIdx + 1, rIdx - 1, s)


sol = Solution()
sol.reverseString(["h","e","l","l","o"])