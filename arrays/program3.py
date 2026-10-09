class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # start your solution
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
        # end your solution

def main():
    m, n = map(int, input().split())
    nums1 = list(map(int, input().split()))

    if n > 0:
        nums2 = list(map(int, input().split()))
    else:
        nums2 = []

    sol = Solution()
    sol.merge(nums1, m, nums2, n)

    print(' '.join(map(str, nums1)))

if __name__ == "__main__":
    main()