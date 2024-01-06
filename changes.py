def changes(A_list):
    # Count for how many times the value in i+1 index needs to be changed.
    changes_count = 0
    for i in range(0, len(A_list)-1):
        # If the value in i index is equal to the value in i+1 index, then loop adds 1 to changes_count and subtracts 10 from the value in i+1 index.
        if A_list[i] == A_list[i+1]:
            changes_count += 1
            A_list[i+1] -= 10 # Subtracts 10 from the value in i+1 index so that the value is negative and cannot appear in the list again.
    return changes_count


if __name__ == "__main__":

    print(changes([1, 1, 2, 2, 2])) # 2
    print(changes([1, 2, 3, 4, 5])) # 0
    print(changes([1, 1, 1, 1, 1])) # 2
    print(changes([3, 3, 5, 1, 4, 2, 1, 2, 1])) # 2