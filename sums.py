# Algorithm that counts all the possible sums from the list.
def sums(items):

    # If the list is empty, then the return zero.
    if len(items) == 0:
        return 0
    
    # Starting index for the second loop
    max_sum = sum(items)

    # Initializing the sum table
    sum_table = [0] * (max_sum + 1)
    sum_table[0] = 1

    # Checks all the possible sums in the items list.
    for num in items:

        # Checks the sums from the biggest to the smallest
        for i in range(max_sum, -1, -1):

            # If the sum_table[i] is 1, then the sum is already counted.
            if sum_table[i] == 1:

                # If the sum is already counted, then the sum + num is also possible sum.
                sum_table[i + num] = 1
    
    # Summing all the unique sums and subtracting the 1, because the sum_table[0] is 1.
    total_sums = sum(sum_table) - 1

    return total_sums

if __name__ == "__main__":
    print(sums([1, 2, 3]))                  # 6
    print(sums([2, 2, 3]))                  # 5
    print(sums([1, 3, 5, 1, 3, 5]))         # 18
    print(sums([1, 15, 5, 23, 100, 55, 2])) # 121

