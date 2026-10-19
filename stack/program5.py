class Solution:
    def makeGood(self, s: str) -> str:
        # start your solution
        stack = []
        for char in s:
            # Check if stack is not empty and the current character 
            # forms a clashing pair with the top of the stack
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
        # end your solution

def main():
    s = input().strip()
    sol = Solution()
    result = sol.makeGood(s)
    print(result)

if __name__ == "__main__":
    main()