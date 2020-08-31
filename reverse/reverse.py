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

    def reverse_list(self, node, prev):
        pass

    def __repr__(self):
        current = self.head
        nodes = []
        while current:
            if current == self.head:
                nodes.append(f"[Head:{current.value}]")
                current = current.next_node
            elif current == self.tail:
                nodes.append(f"[Tail:{current.value}]")
                current = current.next_node
            else:
                nodes.append(f"[{current.value}]")
                current = current.next_node 
            return '-->'.join(nodes)

bst = LinkedList(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(14)
bst.insert(20)


