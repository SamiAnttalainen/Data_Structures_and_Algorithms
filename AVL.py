class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.balance = 0

class AVL:
    def __init__(self) -> None:
        self.balanced_state = True
        self.root = None


    def insert(self, key):
        self.root = self.insert_node(self.root, key)

    def insert_node(self, root_node, node_key):

        if not root_node:
            root_node = AVLNode(node_key)
            self.balanced_state = False

        elif node_key < root_node.key:
            root_node.left = self.insert_node(root_node.left, node_key)
            if not self.balanced_state:
                if root_node.balance >= 0:
                    self.balanced_state = root_node.balance == 1
                    root_node.balance -= 1
                else:
                    if root_node.left.balance == -1:
                        root_node = self.right_rotate(root_node)
                    else:
                        root_node = self.left_right_rotate(root_node)
                    self.balanced_state = True

        elif node_key > root_node.key:
            root_node.right = self.insert_node(root_node.right, node_key)
            if not self.balanced_state:
                if root_node.balance <= 0:
                    self.balanced_state = root_node.balance == -1
                    root_node.balance += 1
                else:
                    if root_node.right.balance == 1:
                        root_node = self.left_rotate(root_node)
                    else:
                        root_node = self.right_left_rotate(root_node)
                    self.balanced_state = True

        return root_node
        
    def right_rotate(self, root_node):
        child_node = root_node.left
        root_node.left = child_node.right
        child_node.right = root_node

        child_node.balance = root_node.balance = 0
        return child_node
    
    def left_rotate(self, root_node):
        child_node = root_node.right
        root_node.right = child_node.left
        child_node.left = root_node

        child_node.balance = root_node.balance = 0
        return child_node

    def right_left_rotate(self, root_node):
            
            child_node = root_node.right
            grandchild_node = child_node.left
            child_node.left = grandchild_node.right
            grandchild_node.right = child_node
            root_node.right = grandchild_node.left
            grandchild_node.left = root_node
            root_node.balance = child_node.balance = 0
    
            if grandchild_node.balance == 1:
                root_node.balance = -1
    
            elif grandchild_node.balance == -1:
                child_node.balance = 1
    
            grandchild_node.balance = 0
    
            return grandchild_node

    def left_right_rotate(self, root_node):

        child_node = root_node.left
        grandchild_node = child_node.right
        child_node.right = grandchild_node.left
        grandchild_node.left = child_node
        root_node.left = grandchild_node.right
        grandchild_node.right = root_node
        root_node.balance = child_node.balance = 0

        if grandchild_node.balance == -1:
            root_node.balance = 1

        elif grandchild_node.balance == 1:
            child_node.balance = -1

        grandchild_node.balance = 0

        return grandchild_node

    def preorder(self):
        

        # If the root is None, then returning None.
        if self.root is None:
            return None

        # Else calling the preorder_node function.
        else:
            self.preorder_node(self.root)
        print()

    def preorder_node(self, node):

        if node:
            
            print(f"{node.key};{node.balance}", end=" ")

            self.preorder_node(node.left)

            self.preorder_node(node.right)



if __name__ == "__main__":
    Tree = AVL()
    for key in [9, 10, 11, 3, 2, 6, 4, 7, 5, 1]:
        Tree.insert(key)
        Tree.preorder()
    Tree.preorder()     # 9 4 2 1 3 6 5 7 10 11
        