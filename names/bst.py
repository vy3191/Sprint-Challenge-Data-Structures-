class BST:
    def __init__(self,value="aaaaaa"):
        self.value = value
        self.left = None
        self.right = None

    def insert(self,value):
        if self.value is None:
            return None

        if self.value < value:
            if self.right is None:
                new_node = BST(value)
                self.right = new_node
            else:
                self.right.insert(value)
        if self.value > value:
            if self.left is None:
                new_node = BST(value)            
                self.left = new_node
            else:
                self.left.insert(value)

    def contains(self,target):
        if self.value is None:
            return None
        if target is None:
            return None
        if self.value == target:
            return True
        if self.value < target:
            if self.right is None:
                return False
            elif self.right == target:
                return True    
            else:
                self.right.contains(target)       
        if self.value > target:
            if self.left is None:
                return False
            elif self.left == target:
                return True    
            else:
                self.left.contains(target)  


