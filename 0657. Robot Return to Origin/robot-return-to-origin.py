class Solution:
    def judgeCircle(self, moves: str) -> bool:
        coord = {'U': 0, 'D': 0, 'L': 0, 'R': 0}
        for move in moves:
            coord[move] += 1
        return coord['U'] == coord['D'] and coord['L'] == coord['R']
