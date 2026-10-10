class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # start your solution
        if not matrix or not matrix[0]:
            return []
        
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
                
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
                
        return result
        # end your solution


def main():
    m, n = map(int, input().split())
    matrix = []
    for _ in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)
        
    sol = Solution()
    result = sol.spiralOrder(matrix)
    
    print(' '.join(map(str, result)))


if __name__ == "__main__":
    main()