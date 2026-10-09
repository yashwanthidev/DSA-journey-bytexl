class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # start your solution
        if len(nums) == 0:
            return 0

        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k
        # end your solution


def main():
    n = int(input())
    nums = list(map(int, input().split()))

    sol = Solution()
    k = sol.removeDuplicates(nums)

    print(k)
    print(' '.join(map(str, nums[:k])))


if __name__ == "__main__":
    main()