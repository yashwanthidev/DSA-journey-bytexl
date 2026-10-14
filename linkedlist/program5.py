class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Dummy node to handle edge cases like head swapping easily
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            # Rearrange the actual node pointers
            first.next = second.next
            second.next = first
            prev.next = second

            # Move prev pointer two nodes ahead
            prev = first

        return dummy.next

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
    n = int(input().strip())
    if n > 0:
        arr = list(map(int, input().split()))
    else:
        arr = []
    
    head = buildList(arr)
    sol = Solution()
    result = sol.swapPairs(head)
    printList(result)

if __name__ == "__main__":
    main()