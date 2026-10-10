class Solution:
    def reverseWords(self, s):
        def reverse(left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        n = len(s)
        start = 0
        for i in range(n):
            if s[i] == ' ':
                reverse(start, i - 1)
                start = i + 1
        reverse(start, n - 1)

        reverse(0, n - 1)

n = int(input())
line = input()

s = []
for ch in line:
    if ch == ' ':
        continue
    elif ch == '_':
        s.append(' ')
    else:
        s.append(ch)

sol = Solution()
sol.reverseWords(s)

print(' '.join('_' if c == ' ' else c for c in s))