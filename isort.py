
# Algorithm that sorts integers in ascending order.
def isort(A_list):

    # Checks that the list is not too big and that the values are not too big in the list.
    if len(A_list) <= 1e3 and max(A_list) <= 1e3:
        
        # While loop swaps the value in j index with the value in j+1 index until the value in j index is smaller than the value in j+1 index.
        for i in range(1, len(A_list)):
            j = i-1
            while (j >= 0) and (A_list[j] > A_list[j+1]): 
                A_list[j], A_list[j+1] = A_list[j+1], A_list[j]
                j = j-1

    return A_list


if __name__ == "__main__":
    A_list = [12, 5, 22, 45, 7, 1, 3, 18, 31]
    isort(A_list)
    print(A_list)

