class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = dict(zip(indices, s))
        final = []
        for i in range(len(s)):
            final.append(result[i])
        return ''.join(final)
