class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        # # start your solution
        def can_split(max_sum: int) -> bool:
            teams_count = 1
            current_sum = 0
            for num in nums:
                if current_sum + num > max_sum:
                    teams_count += 1
                    current_sum = num
                else:
                    current_sum += num
            return teams_count <= k

        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1

        return left
        # # end your solution


def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    sol = Solution()
    result = sol.splitArray(nums, k)

    print(result)


if __name__ == "__main__":
    main()