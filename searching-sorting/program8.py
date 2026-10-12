class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        # start your solution
        def can_ship(capacity: int)->bool:
            days_needed=1
            current_weight=0
            for w in weights:
                if current_weight + w > capacity:
                    days_needed += 1
                    current_weight = w
                else:
                    current_weight += w
            return days_needed <= days
        low = max(weights)
        high = sum(weights)
        ans = high
        while low<=high:
            mid = (low+high)//2
            if can_ship(mid):
                ans = mid
                high = mid -1
            else:
                low = mid + 1
        return ans

        # end your solution


def main():
    n, d = map(int, input().split())
    weights = list(map(int, input().split()))

    sol = Solution()
    result = sol.shipWithinDays(weights, d)

    print(result)

if __name__ == "__main__":
    main()