class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

def main():
    haystack = input().strip()
    needle = input().strip()

    sol = Solution()
    result = sol.strStr(haystack, needle)

    print(result)

if __name__ == "__main__":
    main()