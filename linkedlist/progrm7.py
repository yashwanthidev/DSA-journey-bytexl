import sys


class Node:

  def __init__(self, val: int):
    self.val = val
    self.next = None
    self.random = None


class Solution:

  def copyRandomList(self, head: 'Node') -> 'Node':
    # start your solution
    if not head:
      return None

    # Step 1: Create a new copied node right after each original node
    curr = head
    while curr:
      copy = Node(curr.val)
      copy.next = curr.next
      curr.next = copy
      curr = copy.next

    # Step 2: Assign random pointers for the copied nodes
    curr = head
    while curr:
      if curr.random:
        curr.next.random = curr.random.next
      curr = curr.next.next

    # Step 3: Separate the copied list from the original list
    dummy = Node(0)
    copy_curr = dummy
    curr = head
    while curr:
      copy_node = curr.next
      curr.next = copy_node.next
      copy_curr.next = copy_node

      copy_curr = copy_curr.next
      curr = curr.next

    return dummy.next
    # end your solution


def buildList(values, randomIndices):
  if not values:
    return None
  nodes = [Node(val) for val in values]
  for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]
  for i, idx in enumerate(randomIndices):
    if idx != -1:
      nodes[i].random = nodes[idx]
  return nodes[0]


def printList(head):
  if not head:
    print('empty')
    return
  nodes = []
  current = head
  while current:
    nodes.append(current)
    current = current.next
  print(' '.join(str(node.val) for node in nodes))
  node_to_idx = {node: i for i, node in enumerate(nodes)}
  random_indices = [
      -1 if node.random is None else node_to_idx[node.random] for node in nodes
  ]
  print(' '.join(str(idx) for idx in random_indices))


def main():
  data = sys.stdin.read().strip().split()
  if not data:
    return
  n = int(data[0])
  if n == 0:
    print('empty')
    return
  values = list(map(int, data[1 : 1 + n]))
  randomIndices = list(map(int, data[1 + n : 1 + 2 * n]))
  head = buildList(values, randomIndices)
  sol = Solution()
  copied = sol.copyRandomList(head)
  printList(copied)


if __name__ == '__main__':
  main()