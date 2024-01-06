# Method that returns all subsets of a set of numbers from 1 to n
def subsets(nums: int) -> list:

    # List of subsets
    subsets = [[]]

    # Loop through the numbers from 1 to nums
    for i in range(1, nums + 1):

        # Help list for storing the lists in subsets
        subsets_help = []

        # Loop through the lists in subsets
        for j in range(len(subsets)):

            # Create a copy of the list in subsets
            subsets_help.append(subsets[j].copy())

            # Add the number to the copy of the list
            subsets_help[-1].append(i)

        # Add the lists in subsets_help to subsets
        subsets.extend(subsets_help)
    
    # Removing the empty list from subsets, so that the result is correct.
    subsets.remove([])

    return subsets



if __name__ == "__main__":
    print(subsets(1))   # [[1]]
    print(subsets(2))   # [[1], [2], [1, 2]]
    print(subsets(3))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    print(subsets(4))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3],
                        #  [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4],
                        #  [2, 3, 4], [1, 2, 3, 4]]
    S = subsets(10)
    print(S[95])    # [6, 7]
    print(S[254])   # [1, 2, 3, 4, 5, 6, 7, 8]
    print(S[826])   # [1, 2, 4, 5, 6, 9, 10]