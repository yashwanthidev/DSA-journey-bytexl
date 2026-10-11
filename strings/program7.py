class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0
        read = 0
        n = len(chars)

        while read < n:
            curr_char = chars[read]
            count = 0

            # Count consecutive duplicate characters
            while read < n and chars[read] == curr_char:
                read += 1
                count += 1

            # Write the character to the compressed position
            chars[write] = curr_char
            write += 1

            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write


def main():
    n = int(input())
    chars = input().split()

    sol = Solution()
    new_length = sol.compress(chars)

    print(new_length)
    print(' '.join(chars[:new_length]))


if __name__ == "__main__":
    main()