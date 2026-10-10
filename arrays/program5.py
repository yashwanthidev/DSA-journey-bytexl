class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        # start your solution
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 > nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]

            if nums[left] % 2 == 0:
                left += 1
            if nums[right] % 2 == 1:
                right -= 1

        return nums
        # end your solution


def main():
    n = int(input())
    nums = list(map(int, input().split()))

    sol = Solution()
    result = sol.sortArrayByParity(nums)

    print(' '.join(map(str, result)))


if __name__ == "__main__":
    main()