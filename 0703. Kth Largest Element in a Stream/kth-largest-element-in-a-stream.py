class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.keyword = k
        self.min_q = []
        for x in nums:
            self.add(x)

    def add(self, val: int) -> int:
        heappush(self.min_q, val)
        if len(self.min_q) > self.keyword:
            heappop(self.min_q)
        return self.min_q[0]
