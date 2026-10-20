class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        # start your solution
        ans = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fn_id_str, typ, timestamp_str = log.split(':')
            fn_id = int(fn_id_str)
            timestamp = int(timestamp_str)

            if typ == "start":
                if stack:
                    ans[stack[-1]] += timestamp - prev_time
                stack.append(fn_id)
                prev_time = timestamp
            else:
                ans[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1

        return ans
        # end your solution

def main():
    n = int(input())
    m = int(input())
    logs = []
    for _ in range(m):
        logs.append(input().strip())

    sol = Solution()
    result = sol.exclusiveTime(n, logs)

    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()