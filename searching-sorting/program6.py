class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            total_hours = sum((pile + mid - 1) // mid for pile in piles)

            if total_hours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

def main():
    n, h = map(int, input().split())
    piles = list(map(int, input().split()))

    sol = Solution()
    result = sol.minEatingSpeed(piles, h)

    print(result)

if __name__ == "__main__":
    main()