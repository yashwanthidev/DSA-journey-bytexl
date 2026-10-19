class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        depth = 0
        
        for char in s:
            if char == '(':
                if depth > 0:
                    res.append(char)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    res.append(char)
                    
        return "".join(res)

def main():
    s = input().strip()
    sol = Solution()
    result = sol.removeOuterParentheses(s)
    print(result)

if __name__ == "__main__":
    main()