class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        froms = [x[0] for x in paths]
        to = ''.join([x[1] for x in paths if x[1] not in froms])
        return to
