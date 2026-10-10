class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # start your solution
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
        # end your solution

def main():
    n = int(input())
    prices = list(map(int, input().split()))
    
    sol = Solution()
    result = sol.maxProfit(prices)
    
    print(result)

if __name__ == "__main__":
    main()