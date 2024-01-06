class HashBucket:
    def __init__(self, size, buckets):

        self.size = size
        self.buckets = buckets
        self.values = [None] * size
        self.overflow = [None] * size


    def hash(self, String):
            
        # Calculating the hash index of the string with formula sum = sum + ord(String[i]) and index = sum % buckets.
        sum = 0

        for i in range(len(String)):
            sum+=ord(String[i])

        index = sum % self.buckets
        #print(String + " " + str(index))

        return index



    def insert(self, String):

        # Calculating bucket index.
        index = self.hash(String) * (self.size // self.buckets)


        # If the index is available, then inserting the string to the index.
        for i in range(index, index + (self.size // self.buckets)):
            if self.values[i] is None or self.values[i] == String or self.values[i] == "Tombstone":
                self.values[i] = String
                return
        
        # If the index is not available, then inserting the string to the overflow.
        else:
            for i in range(0, len(self.overflow)-1):
                if self.overflow[i] is None or self.overflow[i] == String:
                    self.overflow[i] = String
                    return
        


    def delete(self, String):

        # Calculating bucket index.
        index = self.hash(String) * (self.size // self.buckets)

        # If the string is in the hash table, then setting the value of the index to "Tombstone".
        for i in range(index, index + (self.size // self.buckets)):
            if self.values[i] == String:
                self.values[i] = "Tombstone"
                return

        # Else looping through the overflow list until the string is found and setting the value to "Tombstone".   
        else:
            for i in range(0, len(self.overflow)-1):
                if self.overflow[i] == String:
                    self.overflow[i] = "Tombstone"
                    return



                 
    def print(self):
        
        # Printing list of values.
        values = []

        # Looping through the values in the hash table and appending them to the list.
        for i in range(0, len(self.values)):
            if self.values[i] != None and self.values[i] != "Tombstone":
                values.append(self.values[i])
        
        # Looping through the values in the overflow list and appending them to the list.
        for i in range(0, len(self.overflow)):
            if self.overflow[i] != None and self.overflow[i] != "Tombstone":
                values.append(self.overflow[i])

        # Printing the list of the strings in the hash table.
        print(" ".join(values))
        return

if __name__ == "__main__":

    table = HashBucket(10, 5)
    table.insert("buttermilk")
    table.insert("shim")
    table.insert("resolvend")
    table.insert("cheiromegaly")
    table.insert("premillennialise")
    table.insert("finebent")
    print("After insertion:") # buttermilk shim resolvend premillennialise cheiromegaly finebent
    table.print()
    table.delete("buttermilk")
    table.delete("cores")
    table.delete("cheiromegaly")
    table.delete("iodations")
    print("After deletion:")
    table.print() # shim resolvend premillennialise finebent
    table.insert("iodations")
    table.insert("tirrlie")
    table.insert("comous")
    table.insert("discursiveness")
    table.insert("flabbergasts")
    table.insert("rename")
    table.insert("softhead")
    print("After insertion:") # iodations discursiveness softhead comous rename shim resolvend premillennialise flabbergasts finebent tirrlie
    table.print()