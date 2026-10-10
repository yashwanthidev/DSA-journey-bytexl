class Solution:
    def reverseString(self, s: list[str]) -> None:
        # start your solution
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        # end your solution

def main():
    n = int(input())
    s = input().split()
    
    sol = Solution()
    sol.reverseString(s)
    
    print(' '.join(s))

if __name__ == "__main__":
    main()