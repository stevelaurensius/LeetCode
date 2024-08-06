class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        word = ''.join([x[0] for x in words])
        return word == s
