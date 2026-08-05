class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            matrix=None
            return
        self.matrix=matrix
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.matrix:
            return 0
        total=0
        for row in range(row1,row2+1):
            for col in range(col1,col2+1):
                total+=self.matrix[row][col]
        return total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)