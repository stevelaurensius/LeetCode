class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        checking_point = []
        
        def is_magic_square(grid):
            flattened_grid = [num for row in grid for num in row]
            if sorted(flattened_grid) != list(range(1, 10)):
                return False
            magic_constant = 15
            for row in grid:
                if sum(row) != magic_constant:
                    return False
            for col in range(3):
                if sum(grid[row][col] for row in range(3)) != magic_constant:
                    return False
            if sum(grid[i][i] for i in range(3)) != magic_constant:
                return False
            if sum(grid[i][2-i] for i in range(3)) != magic_constant:
                return False
            return True

        for i in range(len(grid) - 2):
            for j in range(len(grid[i]) - 2):
                checking_point.append([i, j])
        
        matrix_3x3 = []
        for coord in checking_point:
            first_row = [grid[coord[0]][coord[1]], grid[coord[0]][coord[1] + 1], grid[coord[0]][coord[1] + 2]]
            second_row = [grid[coord[0] + 1][coord[1]], grid[coord[0] + 1][coord[1] + 1], grid[coord[0] + 1][coord[1] + 2]]
            third_row = [grid[coord[0] + 2][coord[1]], grid[coord[0] + 2][coord[1] + 1], grid[coord[0] + 2][coord[1] + 2]]
            matrix_3x3.append([first_row, second_row, third_row])

        result = 0
        for data in matrix_3x3:
            if is_magic_square(data):
                result += 1
            
        return result
