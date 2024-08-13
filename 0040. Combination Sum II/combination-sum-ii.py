class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = set()

        def backtrack(remaining, start, path):
            if remaining == 0:
                result.add(tuple(path))
                return
            if remaining < 0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break
                backtrack(remaining - candidates[i], i + 1, path + [candidates[i]])

        backtrack(target, 0, [])
        return [list(comb) for comb in result]
