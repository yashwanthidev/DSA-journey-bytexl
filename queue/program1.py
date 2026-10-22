def main():
    try:
        line = input().strip()
        while not line:
            line = input().strip()
        n = int(line)
    except (EOFError, ValueError):
        return

    queue = []
    MAX_SIZE = 5

    for _ in range(n):
        try:
            line = input().strip()
            while not line:
                line = input().strip()
        except EOFError:
            break

        parts = line.split()
        if not parts:
            continue

        cmd = parts[0]

        if cmd == "ARRIVE":
            x = parts[1]
            if len(queue) == MAX_SIZE:
                print("Queue Full")
            else:
                queue.append(x)

        elif cmd == "SERVE":
            if not queue:
                print("No Customers")
            else:
                queue.pop(0)

        elif cmd == "FRONT":
            if not queue:
                print("No Customers")
            else:
                print(queue[0])

        elif cmd == "ISEMPTY":
            if len(queue) == 0:
                print("true")
            else:
                print("false")

if __name__ == "__main__":
    main()