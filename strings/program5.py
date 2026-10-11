class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        clean_s = s.replace("-", "").upper()
        if not clean_s:
            return ""

        first_group_len = len(clean_s) % k

        groups = []
        if first_group_len:
            groups.append(clean_s[:first_group_len])

        for i in range(first_group_len, len(clean_s), k):
            groups.append(clean_s[i:i + k])

        return "-".join(groups)

def main():
    s = input().strip()
    k = int(input().strip())

    sol = Solution()
    result = sol.licenseKeyFormatting(s, k)

    print(result)

if __name__ == "__main__":
    main()