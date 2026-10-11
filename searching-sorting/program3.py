class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        low = 0
        high = len(arr) - 1

        while low < high:
            mid = (low + high) // 2
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid

        return low


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    sol = Solution()
    result = sol.peakIndexInMountainArray(arr)

    print(result)


if __name__ == "__main__":
    main()