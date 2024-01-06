def primes(N):
    count = 0 # Number of primes
    multiples_list = []  # List of integer multiples from the loop.
    sqrt_N = int(N**0.5) # Square root of N.
    if 1 <= N <= 1e5: # Checks that N is between 1 and 1e5.
        for i in range(2, N):
            for j in range(2, sqrt_N+1):
                multiples_list.append(i*j) # Adds the multiples of i*j to the multiples list.

        for i in range(2, N+1):
            if i not in multiples_list:
                count += 1
    return count


if __name__ == "__main__":
    print(primes(9999))