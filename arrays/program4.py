class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # start your solution
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
        # end your solution

def main():
    n = int(input())
    digits = list(map(int, input().split()))

    sol = Solution()
    result = sol.plusOne(digits)

    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()