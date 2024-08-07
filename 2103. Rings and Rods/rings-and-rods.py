class Solution:
    def countPoints(self, rings):
        result = 0
        rings_dict = {0:set(), 1:set(), 2:set(), 3:set(), 4:set(), 
        5:set(), 6:set(), 7:set(), 8:set(), 9:set()}
        for i in range(1, len(rings), 2):
            rings_dict[int(rings[i])].add(rings[i-1])
        for i in rings_dict.values():
            if len(i) == 3:
                result += 1
        return result
