# import math

# def modulo(K):
#     return K % 10


# def hash(String):

#     sum = 0

#     for i in range(0, len(String)-1):
#         sum += ord(String[i])

#     return sum%5


# def recursion(x):

#     if x == 0:
#         return 1

#     else:
#         return recursion(x-1) + recursion(x-1)


# # Recursive Python function to solve the tower of hanoi

# def TowerOfHanoi(n , source, destination, auxiliary):
# 	if n==1:
# 		print ("Move disk 1 from source",source,"to destination",destination)
# 		return
# 	TowerOfHanoi(n-1, source, auxiliary, destination)
# 	print ("Move disk",n,"from source",source,"to destination",destination)
# 	TowerOfHanoi(n-1, auxiliary, destination, source)
		


# Contributed By Dilip Jain
def search(k):
    if k == n:
        # Process permutation
        print(numbers)
    else:
        for i in range(1, n + 1):
            if not included[i]:
                included[i] = True
                numbers[k] = i
                search(k + 1)
                included[i] = False

n = 5  # Change this to the desired value of 'n'
numbers = [0] * n
included = [False] * (n + 1)
search(0)



# if __name__ == "__main__":


    #print(recursion(15))


    # TowerOfHanoi(2, "A", "B", "C")

    # print(math.floor(math.log(12,2)))

    # print("Modulo indexes:")
    # print(modulo(27))
    # print(modulo(32))
    # print(modulo(15))
    # print(modulo(77))
    # print(modulo(6))
    # print(modulo(11))
    # print(modulo(22))
    # print(modulo(45))
    # print(modulo(99))
    # print(modulo(40))
    # print("Floor indexes:")
    # print(math.floor(27/10))
    # print(math.floor(32/10))
    # print(math.floor(15/10))
    # print(math.floor(77/10))
    # print(math.floor(6/10))
    # print(math.floor(11/10))
    # print(math.floor(22/10))
    # print(math.floor(45/10))
    # print(math.floor(99/10))
    # print(math.floor(40/10))

    # print("Dog", hash("dog"))
    # print("Cat",hash("cat"))
    # print("Bird", hash("bird"))
    # print("Worm", hash("worm"))
    # print("Fish", hash("fish"))
    # print("Cow",hash("cow"))
    # print("Wolf",hash("wolf"))
    # print("Fox",hash("fox"))
    # print("Seal",hash("seal"))
    # print("Fly",hash("fly"))

    # print(modulo(91))
    # print(modulo(103))
    # print(modulo(79))
    # print(modulo(247))
    # print(modulo(9))