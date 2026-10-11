class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_num = 0
        operation = '+'
        
        for i, char in enumerate(s):
            if char.isdigit():
                current_num = current_num * 10 + int(char)
                
            # If the character is an operator or the last character in the string
            if (not char.isdigit() and char != ' ') or i == len(s) - 1:
                if operation == '+':
                    stack.append(current_num)
                elif operation == '-':
                    stack.append(-current_num)
                elif operation == '*':
                    stack.append(stack.pop() * current_num)
                elif operation == '/':
                    # int(a / b) in Python truncates towards zero (unlike a // b which floors)
                    prev = stack.pop()
                    stack.append(int(prev / current_num))
                
                operation = char
                current_num = 0
                
        return sum(stack)

def main():
    s = input()
    sol = Solution()
    result = sol.calculate(s)
    print(result)

if __name__ == "__main__":
    main()