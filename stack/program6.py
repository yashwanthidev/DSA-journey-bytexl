class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        # start your solution
        stack = []
        nums_k = float('-inf')
        
        for num in reversed(nums):
            if num < nums_k:
                return True
            while stack and stack[-1] < num:
                nums_k = stack.pop()
            stack.append(num)
            
        return False
        # end your solution

def main():
    n = int(input())
    nums = list(map(int, input().split()))

    sol = Solution()
    result = sol.find132pattern(nums)

    print("true" if result else "false")

if __name__ == "__main__":
    main()