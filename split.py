def split(integer_list):

    list_length = len(integer_list)
    split_count = 0

    # The biggest value on the left side of the list. Initalizing the value with the first value of the integer list.
    left_maximum = integer_list[0]

     # List of the smallest values on the right side of the list. Initializing the list with infinity values, so that the loop can compare the values properly.
    right_minimum_list = [float("inf")] * list_length

    # Initializing the last value of the right_minimum_list with the last value of the integer_list.
    right_minimum_list[list_length-1] = integer_list[list_length-1]

    # For loop checks indexes and adds currently the smallest value to the right_minimum_list.
    for i in range(list_length-2, -1, -1):

        # If the current value in integer list is smaller than the previous value in right minimum list, then the current value is added to the right_minimum_list.
        if integer_list[i] < right_minimum_list[i+1]:
            right_minimum_list[i] = integer_list[i]

        # If the current value in integer list is bigger than the previous value in right minimum list, then the previous value is added to the right_minimum_list.
        else:
            right_minimum_list[i] = right_minimum_list[i+1]

    for i in range(0, list_length-1):

        # If the current value is bigger than the left maximum, then the left maximum is changed to the current value.
        if integer_list[i] > left_maximum:
            left_maximum = integer_list[i]

        # If the left maximum is smaller than the smallest value on the right side of the list, then the split count is increased by one.
        if left_maximum < right_minimum_list[i+1]:
            split_count += 1
        
    return split_count



if __name__ == "__main__":

    print(split([1,2,3,4,5]))       # 4
    print(split([5,4,3,2,1]))       # 0
    print(split([2,1,2,5,7,6,9]))   # 3
    print(split([1,2,3,1]))         # 0