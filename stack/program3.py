class Solution:
    def calPoints(self, operations: list[str]) -> int:
        scores = []

        for op in operations:
            if op == "C":
                scores.pop()

            elif op == "D":
                scores.append(scores[-1] * 2)

            elif op == "+":
                scores.append(scores[-1] + scores[-2])

            else:
                scores.append(int(op))

        return sum(scores)


def main():
    n = int(input())
    operations = input().split()

    sol = Solution()
    result = sol.calPoints(operations)

    print(result)


if __name__ == "__main__":
    main()