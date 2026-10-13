class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # start your solution
        if not head or not head.next:
            return True

        # 1. Find the middle node using slow and fast pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half of the list
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # 3. Compare the first half and the reversed second half
        first_half = head
        second_half = prev
        is_palin = True
        while second_half:
            if first_half.val != second_half.val:
                is_palin = False
                break
            first_half = first_half.next
            second_half = second_half.next

        return is_palin
        # end your solution

def buildList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    head = buildList(arr)

    sol = Solution()
    result = sol.isPalindrome(head)

    print("true" if result else "false")

if __name__ == "__main__":
    main()