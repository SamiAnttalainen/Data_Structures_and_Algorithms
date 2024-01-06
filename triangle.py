# Method checks if the given sides form a valid triangle.
def triangle(a_side, b_side, c_side):

    # If statement checks that the sum of two sides is greater than the third side. If not, the triangle is not valid.
    if a_side + b_side <= c_side or a_side + c_side <= b_side or b_side + c_side <= a_side:
        return False
    
    else:
        return True
    


if __name__ == "__main__":
    print(triangle(3, 4, 5))
    print(triangle(-1, 2, 3))
    print(triangle(5, 9, 4))
    print(triangle(30, 12, 29))
    print(triangle(1, 3, 2))
    print(triangle(100, 150, 150))
    print(triangle(900, 1200, 1500))