class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        # If target is >= last element, wrap around to the first letter
        if target >= letters[-1]:
            return letters[0]
        
        low = 0
        high = len(letters) - 1
        ans = letters[0]
        
        while low <= high:
            mid = (low + high) // 2
            
            if letters[mid] > target:
                ans = letters[mid]
                high = mid - 1
            else:
                low = mid + 1
                
        return ans

def main():
    n = int(input())
    letters = input().split()
    target = input().strip()
    
    sol = Solution()
    result = sol.nextGreatestLetter(letters, target)
    
    print(result)

if __name__ == "__main__":
    main()