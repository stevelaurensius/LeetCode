class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        result = []
        for i in range(len(s)):
            result.append(abs(s.index(s[i]) - t.index(s[i])))
        return sum(result)
