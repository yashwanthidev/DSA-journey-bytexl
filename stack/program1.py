import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    idx = 1
    
    stack = []
    MAX_SIZE = 5

    for _ in range(n):
        if idx >= len(input_data):
            break
        
        command = input_data[idx]
        idx += 1
        
        if command == "VISIT":
            page_id = input_data[idx]
            idx += 1
            if len(stack) == MAX_SIZE:
                print("History Full")
            else:
                stack.append(page_id)
                
        elif command == "BACK":
            if not stack:
                print("No Pages")
            else:
                stack.pop()
                
        elif command == "CURRENT":
            if not stack:
                print("No Pages")
            else:
                print(stack[-1])
                
        elif command == "ISEMPTY":
            if not stack:
                print("true")
            else:
                print("false")

if __name__ == "__main__":
    solve()