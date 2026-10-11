class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        # start your solution
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            
            # Ensure mid is at an even index
            if mid % 2 == 1:
                mid -= 1
            
            # If the pair matches, the single element lies to the right
            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                # The pattern broke, so the single element is at mid or to the left
                high = mid
                
        return nums[low]
        # end your solution

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    
    sol = Solution()
    result = sol.singleNonDuplicate(nums)
    
    print(result)

if __name__ == "__main__":
    main()