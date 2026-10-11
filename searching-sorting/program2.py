class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 0
        high = n
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            coins_needed = mid * (mid + 1) // 2
            
            if coins_needed <= n:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans

def main():
    n = int(input())
    sol = Solution()
    result = sol.arrangeCoins(n)
    print(result)

if __name__ == "__main__":
    main()