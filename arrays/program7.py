class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        # start your solution
        n = len(matrix)
        
        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()
        # end your solution

def main():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    sol = Solution()
    sol.rotate(matrix)

    for row in matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()