class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # start your solution
        n = len(nums)
        result = [0] * n
        
        left = 0
        right = n - 1
        pos = n - 1
        
        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            
            if left_square > right_square:
                result[pos] = left_square
                left += 1
            else:
                result[pos] = right_square
                right -= 1
            pos -= 1
            
        return result
        # end your solution

def main():
    n = int(input())
    nums = list(map(int, input().split()))

    sol = Solution()
    result = sol.sortedSquares(nums)

    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()