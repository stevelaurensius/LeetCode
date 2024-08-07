class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        result = [''.join(sorted(x)) for x in words]
        unique = []
        duplicate = []
        for data in result:
            if data not in unique:
                unique.append(data)
            else:
                duplicate.append(data)
        return len(duplicate)
