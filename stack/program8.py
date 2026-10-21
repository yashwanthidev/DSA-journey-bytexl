class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):
            curr_idx = i % n

            while stack and stack[-1] <= nums[curr_idx]:
                stack.pop()

            if i < n and stack:
                res[curr_idx] = stack[-1]

            stack.append(nums[curr_idx])

        return res


def main():
    n = int(input())
    nums = list(map(int, input().split()))

    sol = Solution()
    result = sol.nextGreaterElements(nums)

    print(' '.join(map(str, result)))


if __name__ == "__main__":
    main()