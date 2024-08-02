class Solution:
    def finalValueAfterOperations(self, operations) -> int:
        result = [0]
        for i in operations:
            if i == '--X' or i == 'X--':
                result.append(result[-1] - 1)
            if i == '++X' or i == 'X++':
                result.append(result[-1] + 1)
        return result[-1]
