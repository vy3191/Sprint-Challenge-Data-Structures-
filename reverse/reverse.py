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
        self.count = 0

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)
            self.head = node
        else:
            node.set_next(self.head)
            self.head = node
        self.count += 1        

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
        # if there are no nodes in the Linked list then return None
        if self.head is None:
            return None
        # if there is only one node in the Linked List return it
        elif self.count == 1:    
            return self.head.value
        #if there are more than one node in the Linked List    
        else:
            #Initialize prev = None(given), current=self.head, and next=None
            next = None
            current = self.head
            #Loop through the Linked List while current exists
            while current:
                # grab the current.next value using next
                next = current.next_node
                # change next of current to pre which is default(None)
                current.next_node = prev
                # Move prev and current ahead by one step
                prev = current
                current = next
            self.head = prev    

     
    def __repr__(self):
        current = self.head
        nodes = []
        while current:
            if current is self.head:
                nodes.append(f"[Head:{current.value}]")
                current = current.next_node            
            else:
                nodes.append(f"[{current.value}]")
                current = current.next_node 
        return '-->'.join(nodes)



