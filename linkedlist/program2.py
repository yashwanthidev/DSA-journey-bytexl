class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # start your solution
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
        # end your solution


def buildList(arr):
    if not arr:
        return None
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def printList(head):
    if not head:
        print("empty")
        return
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" ".join(result))


def main():
    line = input().strip()
    if line == "empty":
        head = None
    else:
        arr = list(map(int, line.split()))
        head = buildList(arr)

    sol = Solution()
    result = sol.reverseList(head)
    printList(result)


if __name__ == "__main__":
    main()