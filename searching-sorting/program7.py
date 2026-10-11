class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        nums.sort()
        
        # Helper function: counts how many pairs have a distance <= mid
        def count_pairs(mid: int) -> int:
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count

        # Binary search range for possible distances
        low = 0
        high = nums[-1] - nums[0]

        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low


def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    sol = Solution()
    result = sol.smallestDistancePair(nums, k)

    print(result)


if __name__ == "__main__":
    main()