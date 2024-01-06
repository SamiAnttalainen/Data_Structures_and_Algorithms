class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None
        self.mirrored = False


    def insert(self, key):
        
        if self.mirrored == True:
            self.mirror()
            self.root = self.insert_node(self.root, key)
            self.mirror()


        # Else calling the insert_node function.
        else:
            self.root =  self.insert_node(self.root, key)

    
    def insert_node(self, node, key):

        # If the node is None, then setting the node to key.
        if node == None:
            node = Node(key)
        
        # If the key is smaller than the node key, then setting the left child to key.
        elif key < node.key:
            node.left = self.insert_node(node.left, key)

        # If the key is greater than the node key, then setting the right child to key.
        elif key > node.key:
            node.right = self.insert_node(node.right, key)

        # If the key is equal to the node key, then returning the node.
        return node
    
    def search(self, key):
            
        # If the root is None, then returning None.

        if self.mirrored == True:
            self.mirror()
            node = self.search_node(self.root, key)
            self.mirror()
            return node
            
        # Else calling the search_node function.
        else:
                
            # If the key is equal to the node key, then returning the node.
            return self.search_node(self.root, key)
            
            
    def search_node(self, node, key):
            
        # If the node is None, then returning None.
        if node is None:
            return False
            
        # If the key is smaller than the node key, then calling the search_node function.
        elif key < node.key:
            return self.search_node(node.left, key)
            
        # If the key is greater than the node key, then calling the search_node function.
        elif key > node.key:
            return self.search_node(node.right, key)
            
        else:
            return True


    def remove(self, key):
            
        # If the root is None, then returning None.

        if self.mirrored == True:
            self.mirror()
            self.root = self.remove_node(self.root, key)
            self.mirror()
            
        # Else calling the remove_node function.
        else:
            self.root = self.remove_node(self.root, key)


    def remove_node(self, node, key):

        # If the node is None, then returning None.
        if node is None:
            return None

        # If the key is smaller than the node key, then setting the left child to the return value of the remove_node function.
        elif key < node.key:
            node.left = self.remove_node(node.left, key)

        # If the key is greater than the node key, then setting the right child to the return value of the remove_node function.
        elif key > node.key:
            node.right = self.remove_node(node.right, key)

        # If the key is equal to the node key, then removing the node.
        else:

            # If the node has no children, then setting the node to None.
            # if node.left is None and node.right is None:
            #     node = None

            # If the node has only one child, then setting the node to the child.
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # If the node has two children, then setting the node to the smallest node in the right subtree.
            else:
                node.key = self.biggest(node.left)
                node.left = self.removeMax(node.left)

        # Returning the node.
        return node
    
    def removeMax(self, node):

        if node.right is None:
            return node.left
        
        node.right = self.removeMax(node.right)
        return node

    def smallest(self, node):

        # If the node has no children, then returning the node key.
        if node.left is None:
            return node.key

        # Else calling the smallest function.
        else:
            return self.smallest(node.left)

    def biggest(self, node):

        # If the node has no children, then returning the node key.
        if node.right is None:
            return node.key

        # Else calling the biggest function.
        else:
            return self.biggest(node.right)

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
            
            print(node.key, end=" ")

            self.preorder_node(node.left)

            self.preorder_node(node.right)


    def postorder(self):

        if self.root is None:
            return None
        
        else:
            self.postorder_node(self.root)
        print()


    def postorder_node(self, node):

        if node:

            self.postorder_node(node.left)

            self.postorder_node(node.right)

            print(node.key, end=" ")

    def inorder(self):

        if self.root is None:
            return None
        
        else:
            self.inorder_node(self.root)
        print()

    def inorder_node(self, node):

        if node:

            self.inorder_node(node.left)

            print(node.key, end=" ")

            self.inorder_node(node.right)

    def breadthfirst(self):

        if self.root is None:
            return None
        
        else:
            self.breadthfirst_node(self.root, self.root.key)
        print()

    def breadthfirst_node(self, node, root):
        if node is None:
            return

        # Printing queue
        queue = [node]

        # Loop until the queue is empty
        while queue:

            # Remove the front node from queue and print it
            current_node = queue.pop(0)
            print(current_node.key, end=" ")

            # Adds left or right child of removed node to queue if they are not None
            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

            if current_node == root:
                print()


    def mirror(self):

        if self.root is None and self.mirrored == False:
            self.mirrored = True
            return None
        elif self.root is None and self.mirrored == True:
            self.mirrored = False
            return None

        self.mirror_tree(self.root)
        # Mirrors the tree and sets the mirrored variable to True if it is False and vice versa.
        if self.mirrored == False:
            
            self.mirrored = True
        else:
            
            self.mirrored = False

    def mirror_tree(self, node):
        if node is not None:

            # Swap the left and right children of the current node
            node.left, node.right = node.right, node.left

            # Recursively mirror the left and right subtrees
            self.mirror_tree(node.left)
            self.mirror_tree(node.right)

if __name__ == "__main__":
 
    # Tree = BST()
    # keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    # for key in keys:
    #     Tree.insert(key)

    # print("Preorder after insertion:")
    # Tree.preorder()         # 5 1 3 2 4 9 7 6
    
    # print("Search 6:")
    # print(Tree.search(6))   # True
    # print("Search 8:")
    # print(Tree.search(8))   # False
    
    # print("Preorder after removing 1:")
    # Tree.remove(1)
    # Tree.preorder()         # 5 3 2 4 9 7 6
    # print("Preorder after removing 9:")
    # Tree.remove(9)
    # Tree.preorder()         # 5 3 2 4 7 6 
    # print("Preorder after removing 3:")
    # Tree.remove(3)
    # Tree.preorder()         # 5 2 4 7 6

    # tree = BST()

    # for num in (14, 19, 13, 23, 12, 17, 16, 10, 15, 11, 22, 28, 30, 25, 20):
    #     tree.insert(num)


    # for num in (20, 25, 11, 29, 14):
    #     tree.remove(num)



    # tree.preorder() # 13 12 10 19 17 16 15 23 22 28 30

    # Tree = BST()
    # keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    # for key in keys:
    #     Tree.insert(key)
   
    # Tree.postorder()        # 1 3 2 4 9 7 6 5 or 2 4 3 1 6 7 9 5
    # Tree.inorder()          # 1 2 3 4 5 6 7 9
    # Tree.breadthfirst()     # 5 1 9 3 7 2 4 6

    # Tree = BST()
    # keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    # for key in keys:
    #     Tree.insert(key)

    # Tree.preorder()         # 5 1 3 2 4 9 7 6
    # Tree.mirror()
    # Tree.preorder()         # 5 9 7 6 1 3 4 2 

    # Tree.insert(8)
    # Tree.remove(3)
    # print(Tree.search(2))   # True
    # Tree.preorder()         # 5 9 7 8 6 1 2 4
    # Tree.mirror()
    # Tree.preorder()         # 5 1 2 4 9 7 6 8

    # tree = BST()
    # for num in (14, 19, 13, 23, 12, 17, 16, 10):
    #     tree.insert(num)

    # tree.preorder() # 14 13 12 10 19 17 16 23
    # tree.mirror()
    # for num in (15, 11, 22, 28, 30, 25, 20):
    #     tree.insert(num)

    # tree.preorder() # 14 19 23 28 30 25 22 20 17 16 15 13 12 10 11

    # tree = BST()
    # for num in (14, 19, 13, 23, 12, 17, 16, 10, 15, 11, 22, 28, 30, 25, 20):
    #     tree.insert(num)

    # tree.mirror()
    # for num in (14, 10, 24, 22, 17, 29, 20):
    #     print(tree.search(num))

    # tree.postorder()

    tree = BST()
    for num in (14, 19, 13, 23, 12, 17, 16, 10):
        tree.insert(num)

    tree.preorder()
    tree.mirror()
    for num in (15, 11, 22, 28, 30, 25, 20):
        tree.insert(num)

    tree.preorder()
    #14 13 12 10 19 17 16 23
    #14 19 23 28 30 25 22 20 17 16 15 13 12 10 11


    # True
    # True
    # False
    # True
    # True
    # False
    # True
    # 30 25 28 20 22 23 15 16 17 19 11 10 12 13 14