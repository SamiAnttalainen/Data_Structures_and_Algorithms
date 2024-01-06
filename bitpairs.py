# Algorithm that calculates the sum of the distances between the 1 bits in the bit string.
def pairs(bit_string):

    # List of the indexes of the 1 bits in the bit string.
    index_list = []

    # Adds the index of the 1 bit to the index list, so that we can calculate the distance between the 1 bits.
    for i in range(len(bit_string)):
        if bit_string[i] == '1':
            index_list.append(i)



    # Previous value in the index list is initialized with 0, so that the calculation works properly.
    previous_index_value = 0
    total_bits_length = 0

    # "ones" variable is the sum of distances between 1 bits in the bit string.
    for ones in range(0, len(index_list)):

        # Distance between the 1 bits in the bit string.
        bit_length = (index_list[ones] * ones) - previous_index_value

        # Adds the distance to the total bits length.
        total_bits_length += bit_length

        # Adds the current value to the previous value.
        previous_index_value += index_list[ones]
    
    return total_bits_length



if __name__ == "__main__":

    print(pairs("101")) # 2
    print(pairs("100101")) # 10
    print(pairs("100100111001")) # 71

