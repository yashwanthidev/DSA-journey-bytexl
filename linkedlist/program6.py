class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next or not head.next.next:
            return

        # 1. Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        prev = None
        curr = slow.next
        slow.next = None  # Cut the first half from the second half

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # 3. Interleave/merge the two halves
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

def buildList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def printList(head):
    if not head:
        print("empty")
        return
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next
    print(' '.join(result))

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    head = buildList(arr)

    sol = Solution()
    sol.reorderList(head)

    printList(head)

if __name__ == "__main__":
    main()