class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Phase 1: Finding the intersection point in the cycle
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        # Phase 2: Finding the entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    
    sol = Solution()
    result = sol.findDuplicate(nums)
    
    print(result)

if __name__ == "__main__":
    main()