class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        a = sorted(target)
        b = sorted(arr)
        return True if a == b else False
