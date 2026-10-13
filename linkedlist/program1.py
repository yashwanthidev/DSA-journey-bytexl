class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        # Copy next node's value and bypass it
        node.val = node.next.val
        node.next = node.next.next

def buildList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def findNode(head, val):
    current = head
    while current:
        if current.val == val:
            return current
        current = current.next
    return None

def printList(head):
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next
    print(' '.join(result))

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    target = int(input())

    head = buildList(arr)
    node = findNode(head, target)

    sol = Solution()
    sol.deleteNode(node)

    printList(head)

if __name__ == "__main__":
    main()