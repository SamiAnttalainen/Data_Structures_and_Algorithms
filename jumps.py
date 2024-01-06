# Algorithm that calculates the number of ways to reach the target level by jumping up the levels.
def jumps(n_size, a_jump, b_jump):

    # If the target level is negative or the jump lengths are negative, then return zero jumps.
    if n_size < 0 or a_jump < 0 or b_jump < 0:
        return 0
    
    # If both jump lengths are zero, then return zero jumps.
    if a_jump == 0 and b_jump == 0:
        return 0
    
    # If the target level is zero, then return zero jumps.
    if n_size == 0:
        return 0
    
    # Initializing the jump table
    jump_table = [0] * (n_size + 1)
    jump_table[0] = 1

    # Checks all the possible jumps
    for num in range(1, n_size + 1):

        # If jump is smaller than or equal to the target level, then add the difference of the target level and the jump to the jump_table[num].
        if a_jump <= num:
            jump_table[num] += jump_table[num - a_jump]

        if b_jump <= num:
            jump_table[num] += jump_table[num - b_jump]

    # The total number of jumps is the last item in the jump_table.
    total_jumps = jump_table[-1]
    
    return total_jumps




if __name__ == "__main__":
    print(jumps(4, 1, 2))  # 5
    print(jumps(8, 2, 3)) # 4
    print(jumps(11, 6, 7)) # 0
    print(jumps(30, 3, 5)) # 58
    print(jumps(100, 4, 5)) # 1167937
