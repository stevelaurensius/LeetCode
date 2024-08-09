class Solution:
    def generateTheString(self, n: int) -> str:
        return 'x' * (n - 1) + 'y' if n % 2 == 0 else 'x' * n
