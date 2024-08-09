class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s_set = set(s)
        counter = {x : s.count(x) for x in s_set}
        return len(set(counter.values())) == 1
