def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    output = []

    for char in expression.strip():

        if char.isupper():
            output.append(char)

        elif char == '(':
            stack.append(char)

        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())

            if stack and stack[-1] == '(':
                stack.pop()

        elif char in precedence:
            while (stack and stack[-1] in precedence
                   and precedence[stack[-1]] >= precedence[char]):
                output.append(stack.pop())

            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(output)


expression = input().strip()
print(infix_to_postfix(expression))