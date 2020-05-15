class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    # bug I ran into here was figuring out how to stop the recursion,
    # used brute force to get that portion
    # I need to practice asking more questions, and trying to understand
    # the whole picture of the problem first
    def reverse_list(self, node, prev):
        # must use recursion
        # and the recursion stopper is...when the node is none
        if node is None:
            self.head = prev
            return
        # if linked list is:
        # 1 -> 2 -> 3 -> 4
        # output should be:
        # 4 -> 3 -> 2 -> 1
        swapping_node = node.next_node  # if node is 1, then this is 2
        node.next_node = prev  # if node is 1, then 1's next node is None
        prev = node  # if node is 1, new prev arg will be 1
        node = swapping_node  # new node arg will be 2
        # output round 1 would be
        # 1 -> None
        # and then redoing the process of
        # placing the node's prev value as it's new next value
        self.reverse_list(node, prev)
        # round two args (2, 1)
        # round two output
        # 2 -> 1 -> None
