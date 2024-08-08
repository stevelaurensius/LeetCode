class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        r, c = rStart, cStart
        result = [[r, c]]
        direction_x, direction_y, step_length, step_counter = 0, 1, 0, 0
        while len(result) < rows * cols:
            r = r + direction_x
            c = c + direction_y
            step_counter = step_counter + 1
            if 0 <= r < rows and 0 <= c < cols:
                result.append([r, c])
            if step_counter == step_length // 2 + 1:
                direction_x, direction_y, step_length, step_counter = direction_y, -direction_x, step_length + 1, 0
        return result
