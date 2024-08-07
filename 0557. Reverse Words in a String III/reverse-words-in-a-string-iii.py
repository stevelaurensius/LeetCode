class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        result = [x[-1::-1] for x in a]
        return ' '.join(result)