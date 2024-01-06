class HashLinear:

    def __init__(self, size):
        self.size = size
        self.keys = [None] * size


    def hash(self, String):


        # Calculating the hash index of the string with formula sum = sum + ord(String[i]) and index = sum % size.
        sum = 0
        X = self.size
        for i in range(len(String)):
            sum+=ord(String[i])
        index = sum % X
        #print(String + " " + str(index))
        return index


    def insert(self, String):
        # Calculating the index of the string in the hash table with formula index = sum % size.
        index = self.hash(String)
        #print(sum, index)

        if self.keys[index] is None or self.keys[index] == String or self.keys[index] == "Tombstone":
            self.keys[index] = String
            return

        # If the index is already taken, then finding the next available index.
        else:
            i = 1
            while True:

                new_index = (index + i) % self.size

                # If the index is available, then inserting the string to the index.
                if self.keys[new_index] is None or self.keys[new_index] == String or self.keys[new_index] == "Tombstone":
                    self.keys[new_index] = String
                    return
                
                elif i == self.size:
                    return
                # Else incrementing the index by one.
                else:
                    i += 1

    def delete(self, String):

        index = self.hash(String)

        # If the string is in the hash table, then setting the value of the index to "Tombstone".
        if self.keys[index] == String:
            self.keys[index] = "Tombstone"
            return
        # Else looping the hash table until the string is found or the index is None.
        else:
            i = 1
            while True:

                new_index = (index + i) % self.size

                # If the string is in the hash table, then setting the value of the index to "Tombstone".
                if self.keys[new_index] == String:
                    self.keys[new_index] = "Tombstone"
                    return

                # If the index is None, then the string is not in the hash table.
                elif self.keys[new_index] is None:
                    return
                # If the index is equal to the size of the hash table, then the string is not in the hash table.
                elif i == self.size:
                    return
                # Else incrementing the index by one.
                else:
                    i += 1


    def print(self):

        ordered_keys = []

        # Looping the keys in the hash table and appending the keys to the list.
        for i in range(self.size):

            # If the key is not None, then appending the key to the list.
            if self.keys[i] is not None and self.keys[i] != "Tombstone":
                ordered_keys.append(self.keys[i])

        # Printing the list of the strings in the hash table.
        print(" ".join(ordered_keys))
        return

if __name__ == "__main__":
    table = HashLinear(10)
    table.insert("buttermilk")
    table.insert("shim")
    table.insert("resolvend")
    table.insert("cheiromegaly")
    table.insert("premillennialise")
    table.insert("finebent")
    print("After insertion:")
    table.print() # buttermilk shim cheiromegaly finebent resolvend premillennialise
    table.delete("buttermilk")
    table.delete("cores")
    table.delete("cheiromegaly")
    table.delete("iodations")
    print("After deletion:")
    table.print() # shim finebent resolvend premillennialise
    table.insert("iodations")
    table.insert("tirrlie")
    table.insert("comous")
    table.insert("discursiveness")
    table.insert("flabbergasts")
    table.insert("rename")
    table.insert("softhead")
    print("After insertion:")
    table.print() # iodations discursiveness comous shim tirrlie finebent flabbergasts rename resolvend premillennialise
    


        