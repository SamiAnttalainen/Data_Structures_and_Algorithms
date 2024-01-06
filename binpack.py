# Method that gives approximate solution to the bin packing problem
def binpack(thrash_list, bin_size):

    # Checks if the bin size is valid
    if bin_size <= 0:
        return
    
    # Checks if the thrash list is empty
    if len(thrash_list) == 0:
        return

    # Sorts the items in the thrash list in descending order to make the algorithm more efficient
    thrash_list.sort(reverse=True)

    # List that contains the bins
    bins = [[]]

    # Adds sublist to the bins list if the item fits in the bin
    for item in thrash_list:
        for bin in bins:
            if sum(bin) + item <= bin_size:
                bin.append(item)
                break
        else:
            bins.append([item])
    
    # Returns the list of possible bins
    return bins



if __name__ == "__main__":

    thrash_list = [9, 3, 3, 6, 10, 4, 6, 8, 6, 3]
    B = 10

    bins = binpack(thrash_list, B)

    for i in range(len(bins)):
        print(f"bin {i+1}: {bins[i]}")

# A possible output:
#   bin 1: [9]
#   bin 2: [3, 3, 4]
#   bin 3: [6, 3]
#   bin 4: [10]
#   bin 5: [6]
#   bin 6: [8]
#   bin 7: [6]