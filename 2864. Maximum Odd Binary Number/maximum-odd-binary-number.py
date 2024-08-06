class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s_list = sorted(list(s), reverse=True)
        s_list.append(s_list.pop(0))
        return ''.join(s_list)
