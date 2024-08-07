class Solution:
    def countKeyChanges(self, s: str) -> int:
        s_list = []
        result = 0
        for char in s:
            if s_list == []:
                s_list.append(char.lower())
            if char.lower() != s_list[-1]:
                result += 1
                s_list.append(char.lower())
        return result
