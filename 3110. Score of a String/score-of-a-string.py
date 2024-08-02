class Solution:
    def scoreOfString(self, s: str):
        s_list = [ord(s) for s in list(s)]
        result = []
        for i in range(len(s_list) - 1):
            result.append(abs(s_list[i] - s_list[i + 1]))
        return sum(result)
