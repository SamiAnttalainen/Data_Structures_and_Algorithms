def knapsack(items, K):
    table = [[""] * (K + 1) for _ in range(len(items))]
    table[0][0] = "O"           # OMIT
    table[0][items[0]] = "I"    # INCLUDE
    for i in range(1, len(items)):
        table[i][0] = "O"
        for k in range(1, K + 1):
            if k >= items[i] and table[i - 1][k - items[i]] != "":        
                table[i][k] += "I"
            if table[i - 1][k] != "":
                table[i][k] += "O"
    return table


print(knapsack([5, 2, 3, 7, 1], 8))
print()
print(knapsack([9, 2, 7, 4, 1], 10))