class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # start your solution
        if not headA or not headB:
            return None

        ptrA = headA
        ptrB = headB

        while ptrA != ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA

        return ptrA
        # end your solution


def buildIntersectingLists(arrA, arrB, skipA, skipB):
    if skipA == -1 or skipB == -1:
        headA = buildList(arrA)
        headB = buildList(arrB)
        return headA, headB

    headA = ListNode(arrA[0])
    currA = headA
    for i in range(1, len(arrA)):
        currA.next = ListNode(arrA[i])
        currA = currA.next

    intersectNode = headA
    for _ in range(skipA):
        intersectNode = intersectNode.next

    if skipB == 0:
        headB = intersectNode
    else:
        headB = ListNode(arrB[0])
        currB = headB
        for i in range(1, skipB):
            currB.next = ListNode(arrB[i])
            currB = currB.next
        currB.next = intersectNode

    return headA, headB


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
    n1, n2 = map(int, input().split())
    arrA = list(map(int, input().split()))
    arrB = list(map(int, input().split()))
    skipA = int(input())
    skipB = int(input())

    headA, headB = buildIntersectingLists(arrA, arrB, skipA, skipB)

    sol = Solution()
    result = sol.getIntersectionNode(headA, headB)

    print(result.val if result else "null")


if __name__ == "__main__":
    main()