class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = len([stone for stone in stones if stone in jewels])
        return result
