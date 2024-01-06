# Constants for the indexes.
ZERO = 0
ONE = 1

class Node:
    # Initializing the node with the data that contains integer value of the node and next that contains the next node. 
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None
    

class LinkedList:
    # Initializing the linked list with the head and the tail of the linked list.
    def __init__(self):
        self.head = None
        self.tail = None
        
    # Adds a new node to the end of the linked list.
    def append(self, data):

        # If the linked list is empty, the new node is the head and the tail.
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        
        # If the linked list is not empty, the new node added to the tail.
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        return


    # Inserting a new node to the linked list to the index position.
    def insert(self, data, index):
        

        # Initializing the new node with the data and the current node with the head and current index with 0.
        new_node = Node(data)
        current_node = self.head
        previous_node = None
        current_node_index = ZERO

        # If the index is 0, then the new node is the head and the head is the next node.
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # While loop moves the current node until current node index = parameter index.
        while current_node_index < index:
            
            # Checks that the index is not out of range.
            if current_node.next is not None:
                previous_node = current_node
                current_node = current_node.next
                current_node_index += 1

            # If the index is out of range, then the new node is the tail.
            else:
                return

        previous_node.next = new_node
        new_node.next = current_node
        return

    # Deleting a node from the linked list from the index position.
    def delete(self, index):

        # If the index is 0, then overwrite the head with the next node and return the data of the deleted node.
        if index == 0:
            data = self.head.data
            self.head = self.head.next
            return data

        # Initializing the current node with the head and the previous node with None and the current index with 0.
        current_node = self.head
        previous_node = None
        current_node_index = ZERO

        # While loop moves the current node until current index = parameter index.
        while current_node_index < index:

            # Checks that the index is not out of range.
            if current_node.next:
                previous_node, current_node = current_node, current_node.next
                current_node_index += 1

            # If the index is out of range, then returns None.    
            else:
                return None

        # Overwrites the next value of the previous node with the next value of the current node aka deletes node at the current index.
        previous_node.next = current_node.next

        # Returns the data of the deleted node.
        return current_node.data

    # Printing all the nodes in the linked list.
    def print(self):
        
        # Initializing the current node to the head.
        current_node = self.head

        # While loop prints the data of the current node and moves to the next node until the current node is None.
        while current_node:
            if current_node.next:
                print(current_node.data, end=" -> ")
            else:
                print(current_node.data)
            current_node = current_node.next

    # Returns the index of the node in the linked list.
    def index(self, data):
        current_node = self.head
        current_node_index = ZERO

        # If the data is in the linked list, returns the index of the data, else loops through the linked list.
        while current_node:
            if current_node.data == data:
                return current_node_index
            current_node = current_node.next
            current_node_index += 1

        # If the data is not in the linked list, returns -1.
        return -1
        
    # Swaps the nodes in the linked list with the given indexes.
    def swap(self, index1, index2):

        # If the indexes are the same, then does not swap.
        if index1 == index2:
            return
        
        # If the first index is bigger than the second index, then swaps the indexes.
        if index1 > index2:
            index1, index2 = index2, index1

        # Initializing current indexes to 0 and current nodes to the head.
        current_node_index_1 = ZERO
        current_node_index_2 = ZERO
        current_node_1 = self.head
        current_node_2 = self.head
        previous_node_1 = current_node_1.previous
        previous_node_2 = current_node_2.previous



        # While loop moves the current nodes until current index = parameter index or the next node is None.
        while current_node_index_1 < index1 and current_node_1.next:

            # Swaps the previous and current nodes.
            previous_node_1, current_node_1 = current_node_1, current_node_1.next

            # Increases the current index by 1.
            current_node_index_1 += 1

        # Same as above.
        while current_node_index_2 < index2 and current_node_1.next:
            previous_node_2, current_node_2 = current_node_2, current_node_2.next
            current_node_index_2 += 1


        # If the previous node is not None, then swaps the next values of the previous nodes, else swaps head with the other node.
        if previous_node_1:
            previous_node_1.next = current_node_2
        else:
            self.head = current_node_2

        if previous_node_2:
            previous_node_2.next = current_node_1
        else:
            self.head = current_node_1

        # Swaps the next values of the current nodes.
        current_node_1.next, current_node_2.next = current_node_2.next, current_node_1.next

        return


    def isort(self):

        # If the linked list is empty, then does not sort.
        if self.head is None:
            return

        # Initializing current node to the head, next node to the next node of the head node.
        current_node = self.head
        next_node = self.head.next

        current_node_index = ZERO
        next_node_index = ONE

        # While loop moves the next node until the next node is None.
        while next_node:

            if current_node.data > next_node.data:

                # If the current node is bigger than the next node, then swaps the nodes with the swap function.
                self.swap(current_node_index, next_node_index)

                # Initializes the current node to the head node and next node to the next node of the head node, so that loop starts from the beginning.
                current_node, next_node = self.head, self.head.next

                # Resets the indexes.
                current_node_index, next_node_index = ZERO, ONE
                

            else:
                # If the current node is not bigger than the next node, then moves all the nodes to the next node.
                current_node, next_node = current_node.next, next_node.next
                
                # Increasesing the indexes by 1.
                current_node_index, next_node_index = current_node_index + 1, next_node_index + 1
        return



    


if __name__ == "__main__":
    L1 = LinkedList()
    L1.append(30)
    L1.append(51)
    L1.append(32)
    L1.append(43)
    L1.append(71)
    L1.append(11)
    L1.append(48)
    L1.append(26)
    L1.append(68)
    L1.append(77)
    L1.print()
    L1.isort()
    L1.print()
    print(L1.delete(0))
    

            # # If the current node is bigger than the next node, then swaps the next nodes.
            # if current_node.data > next_node.data:
            #     current_node.next, next_node.next = next_node.next, current_node.next

            #     # If the previous node is not None, then swaps the previous node's next value to the next node.
            #     if previous_node:
            #         previous_node.next = next_node

            #     # If the previous node is None, then initializes the head to the next node.
            #     else:
            #         self.head = next_node

            #     # Initializes the current node to the head node and next node to the next node of the head node, so that loop starts from the beginning.
            #     current_node = self.head
            #     next_node = self.head.next

            # # If the current node is not bigger than the next node, then moves all the nodes to the next node.    
            # else:
            #     previous_node = current_node
            #     current_node = current_node.next
            #     next_node = next_node.next