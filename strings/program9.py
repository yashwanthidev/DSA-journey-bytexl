class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        # start your solution
        res = []
        i = 0
        n = len(words)

        while i < n:
            # Find how many words fit on the current line
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            line_words = words[i:j]
            num_words = len(line_words)

            # Last line or single word in the line -> Left-justified
            if j == n or num_words == 1:
                line_str = " ".join(line_words)
                line_str += " " * (maxWidth - len(line_str))
                res.append(line_str)
            else:
                # Fully justified
                total_letters = sum(len(w) for w in line_words)
                total_spaces = maxWidth - total_letters
                num_gaps = num_words - 1

                base_spaces = total_spaces // num_gaps
                extra_spaces = total_spaces % num_gaps

                line_str = ""
                for k in range(num_gaps):
                    line_str += line_words[k]
                    spaces_to_add = base_spaces + (1 if k < extra_spaces else 0)
                    line_str += " " * spaces_to_add
                line_str += line_words[-1]

                res.append(line_str)

            i = j

        return res
        # end your solution


def main():
    n = int(input())
    words = input().split()
    maxWidth = int(input())

    sol = Solution()
    result = sol.fullJustify(words, maxWidth)

    for line in result:
        print(line)


if __name__ == "__main__":
    main()