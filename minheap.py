class MinHeap:

    def __init__(self, input_list):
        self.size = len(input_list)
        self.storage = input_list[:]
        for i in range(self.size // 2, -1, -1):
            self.heap_down(i)


    def get_parent_index(self, index):
        return (index - 1) // 2
    
    def get_left_child_index(self, index):
        return 2 * index + 1
    
    def get_right_child_index(self, index):
        return 2 * index + 2
    
    def has_parent(self, index):
        return self.get_parent_index(index) >= 0
    
    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size
    
    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size
    
    def parent(self, index):
        return self.storage[self.get_parent_index(index)]
    
    def left_child(self, index):
        return self.storage[self.get_left_child_index(index)]
    
    def right_child(self, index):
        return self.storage[self.get_right_child_index(index)]
    
    def swap(self, index_1, index_2):
        self.storage[index_1], self.storage[index_2] = self.storage[index_2], self.storage[index_1]

    # def insert(self, list):

    #     self.size = len(list)
    #     self.storage = list[:]
    #     for i in range(self.size // 2, -1, -1):
    #         self.heap_down(i)

    def push(self, value):

        if self.size == len(self.storage):
            self.storage.append(value)
            self.size += 1
            self.heap_up(self.size - 1)

        else:
            self.storage[self.size] = value
            self.size += 1
            self.heap_up(self.size - 1)
        
    

    def heap_up(self, index):

        if self.has_parent(index) and self.parent(index) > self.storage[index]:
            self.swap(self.get_parent_index(index), index)
            self.heap_up(self.get_parent_index(index))

    def pop(self):

        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heap_down(0)
        return data
    
    def heap_down(self, index):
        smallest = index

        if self.has_left_child(index) and self.storage[smallest] > self.left_child(index):
            smallest = self.get_left_child_index(index)

        if self.has_right_child(index) and self.storage[smallest] > self.right_child(index):
            smallest = self.get_right_child_index(index)

        if smallest != index:
            self.swap(index, smallest)
            self.heap_down(smallest)

        

    def print(self):
        
        for i in range(0, self.size):
            print(self.storage[i], end=" ")
        print()

if __name__ == "__main__":
    # heap = MinHeap([4, 8, 6, 5, 1, 2, 3])
    # heap.print()        # 1 4 2 5 8 6 3 
    # print(heap.pop())   # 1
    # heap.push(9)
    # heap.print()        # 2 4 3 5 8 6 9

    heap = MinHeap([778, 128, 988, 132, 890])
    _ = heap.print()

    for _ in range(3):
        print(heap.pop())

    _ = [heap.push(num) for num in (675, 755, 282, 794, 494)]
    _ = heap.print() # 282 675 494 988 755 890 794

    

