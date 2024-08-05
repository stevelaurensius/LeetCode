class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arr_counter = Counter(arr)
        result = [x for x in arr if arr_counter[x] == 1]
        try:
            return result[k - 1]
        except IndexError:
            return ''
