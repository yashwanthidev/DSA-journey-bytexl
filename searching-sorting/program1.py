pick = 0

def guess(num: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        # start your solution
        low = 1
        high = n
        
        while low <= high:
            mid = low + (high - low) // 2
            res = guess(mid)
            
            if res == 0:
                return mid
            elif res == -1:
                high = mid - 1
            else:
                low = mid + 1
                
        return -1
        # end your solution

def main():
    global pick
    n = int(input())
    pick = int(input())
    
    sol = Solution()
    result = sol.guessNumber(n)
    
    print(result)

if __name__ == "__main__":
    main()