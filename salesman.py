from queue import PriorityQueue

# Method that uses the branch and bound algorithm to find the shortest path in traveling salesman problem
def salesman(city_map):

    # Checking if the city map is empty
    if len(city_map) == 0:
        return []

    # Adjacency matrix of the city map
    adj_matrice = adj_matrix(city_map)

    # Calculating the lower bound for the cost of the path
    lr_bound = 0
    for i in range(len(adj_matrice)):
        lr_bound += (min(adj_matrice[i]) + min(adj_matrice[j][i] for j in range(len(adj_matrice)) if j != i))
    lr_bound = (lr_bound // 2) + (lr_bound & 1)

    # Initializing the marked_city list, city_path list and the queue
    marked_city = [False] * len(adj_matrice)
    marked_city[0] = True
    city_path = [0]
    queue = PriorityQueue()
    queue.put((0, city_path, marked_city, 0, lr_bound))


    while not queue.empty():

        # Pops the first item from the queue
        _, city_path, marked_city, cost, _ = queue.get()

        # If all the cities have been visited, then return the path
        if len(city_path) == len(adj_matrice):
            city_path.append(city_path[0])
            return city_path

        # If all the cities have not been visited, then add the next city to the queue
        city = city_path[-1]
        for i in range(len(adj_matrice)):
            if not marked_city[i]:
                new_visited_cities = city_path[:]
                new_visited_cities.append(i)
                new_visited = marked_city[:]
                new_visited[i] = True
                new_cost = cost + adj_matrice[city][i]
                new_bound = lr_bound + adj_matrice[city][i] - min(adj_matrice[city])
                queue.put((new_bound, new_visited_cities, new_visited, new_cost, new_bound))

    # If the queue is empty, then return an empty list
    # return []

# Method that creates an adjacency matrix from a city map
def adj_matrix(city_map):
    adj_matrix = []
    for i in range(len(city_map)):
        adj_matrix.append([])
        for j in range(len(city_map[i])):
            adj_matrix[i].append(city_map[i][j])
    return adj_matrix

if __name__ == "__main__":
    city_map = [
        [ 0, 12, 19, 16, 29],
        [12,  0, 27, 25,  5],
        [19, 27,  0,  8,  4],
        [16, 25,  8,  0, 14],
        [29,  5,  4, 14,  0]
    ]

    path = salesman(city_map)
    cost = 0
    for i in range(len(city_map)):
        cost += city_map[path[i]][path[i+1]]

    print(path)     # [0, 1, 4, 2, 3, 0]
    print(cost)     # 45







# def salesman(city_map):



#     length = len(city_map)
#     marked_city = [0] * length
#     path = [0]
#     visited[0] = 1
#     min_value = 1000
#     min_index = 0

#     for _ in range(length - 1):
#         for j in range(length):
#             if city_map[min_index][j] > 0 and city_map[min_index][j] < min_value and visited[j] == 0:
#                 min_value = city_map[min_index][j]
#                 next_index = j
#         min_index = next_index
#         visited[min_index] = 1
#         path.append(min_index)
#         min_value = 1000
#     path.append(0)
#     return path

    # length = len(city_map)
    # path = [0]
    # visited = [0] * length

    # i = 0
    # j = 0
    # min_value = 1000
    # min_index = 0

    # for i in range(length):
    #     for j in range(length):
    #         if city_map[i][j] > 0 and city_map[i][j] < min_value and visited[j] == 0:
    #             min_value = city_map[i][j]
    #             min_index = j
    #         if min_index != 0 and j == length - 1:
    #             path.append(min_index)
    #             visited[min_index] = 1
    #             i = min_index
    #             j = 0
    #             min_value = 1000
    #             continue
    #         if j == length - 1 and min_index == 0:
    #             path.append(min_index)
    #             break
    # return path


# if __name__ == "__main__":
    
#     cost = 0

#     city_map = [
#     #     0   1   2   3   4
#         [ 0, 12, 19, 16, 29],   # 0
#         [12,  0, 27, 25,  5],   # 1
#         [19, 27,  0,  8,  4],   # 2
#         [16, 25,  8,  0, 14],   # 3
#         [29,  5,  4, 14,  0]    # 4
#         ]

#     path = salesman(city_map)
#     for i in range(len(city_map)):
#         cost += city_map[path[i]][path[i+1]]
    
#     print(path)     # [0, 1, 4, 2, 3, 0]
#     print(cost)     # 45