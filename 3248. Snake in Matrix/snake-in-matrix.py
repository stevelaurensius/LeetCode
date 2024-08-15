class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        position = [0, 0]
        for command in commands:
            match command:
                case 'RIGHT':
                    position[1] += 1
                case 'LEFT':
                    position[1] -= 1
                case 'UP':
                    position[0] -= 1
                case 'DOWN':
                    position[0] += 1
        result = (position[0] * n) + position[1]
        return result
