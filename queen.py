def queen(n, m):
    def search(y, placed_queens):
        if placed_queens == m:
            return 1
        if y == n:
            return 0

        count = 0

        for x in range(n):
            if placed(y, x):
                location[y] = x
                count += search(y + 1, placed_queens + 1)
                location[y] = -1  # Reset the placement for backtracking

        count += search(y + 1, placed_queens)

        return count

    def placed(y, x):
        for i in range(y):
            if location[i] == x or abs(location[i] - x) == abs(i - y):
                return False
        return True

    global counter
    counter = 0
    location = [-1] * n
    return search(0, 0)

if __name__ == "__main__":
    print(queen(4, 4))  # 2
    print(queen(4, 2))  # 44
    print(queen(6, 4))  # 982
    print(queen(7, 2))  # 700
    print(queen(8, 8))  # 92

