class Solution:
    def countAsterisks(self, s: str) -> int:
        s_list = s.split('|')
        result = []
        for i in range(0,len(s_list),2):
            result.append(s_list[i].count('*'))
        return sum(result)