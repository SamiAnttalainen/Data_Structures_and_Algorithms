def sales(car_list, customer_list):

    # Sort the lists in ascending order
    cars = sorted(car_list)
    customers = sorted(customer_list)


    # If the budjet of the first customer is lower than the cheapest car, then remove the customer from the list
    if customers[0] < cars[0]:
        customers.pop(0)

    # If the budjet of the richest customer is lower than the most expensive car, then remove the most expensive car from the list
    if customers[-1] < cars[-1]:
        cars.pop(-1)

    i = 0
    j = 0
    sales = 0
    while True:

        # If we have gone through all the customers or all the cars, then break the loop
        if i >= len(customers) or j >= len(cars):
            break
        
        # If the customer can afford the car, then increase the sales and move to the next customer and car
        if customers[i] >= cars[j]:
            sales += 1
            i += 1
            j += 1

        # If the customer can't afford the car, then move to the next customer
        else:
            i += 1
    
    return sales


if __name__ == "__main__":
    print(sales([20, 10, 15], [11, 25, 15]))                        # 3
    print(sales([13, 7, 2, 3, 12, 4, 19], [3, 25, 16, 14]))         # 4
    print(sales([24, 6, 20, 21, 12, 5], [25, 1, 24, 15]))           # 3
    print(sales([14, 9, 10, 15, 18, 20], [24, 17, 9, 22, 12, 4]))   # 5





