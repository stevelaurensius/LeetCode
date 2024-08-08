class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        result = []
        min, max = 0, len(s)
        for i in s:
            match i:
                case 'I':
                    result.append(min) ; min += 1
                case 'D':
                    result.append(max) ; max -= 1
        return result + [min]
