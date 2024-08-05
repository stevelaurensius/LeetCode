class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = [len(x.split()) for x in sentences]
        return max(result)
