class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        # start your solution
        m = len(matrix)
        n = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check if first row contains zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Check if first column contains zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Update inner cells based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Update first row if it originally had a zero
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Update first column if it originally had a zero
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
        # end your solution


def main():
    m, n = map(int, input().split())
    matrix = []
    for _ in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)

    sol = Solution()
    sol.setZeroes(matrix)

    for row in matrix:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    main()