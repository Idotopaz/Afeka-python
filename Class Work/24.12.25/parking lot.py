def park_car(parking_lot, the_car):
    for i in range(len(parking_lot)):
        for j in range(len(parking_lot[i])):
            if parking_lot[i][j] == "":
                parking_lot[i][j] = the_car
                return True
    return False


def remove_car(parking_lot, the_car):
    for i in range(len(parking_lot)):
        for j in range(len(parking_lot[i])):
            if parking_lot[i][j] == the_car:
                parking_lot[i][j] = ""
                return True
    return False


def print_parking_lot(parking_lot):
    for i in range(len(parking_lot)):
        print("|", end="")
        for j in range(len(parking_lot[i])):
            if parking_lot[i][j] == "":
                print("|".rjust(7), end="")
            else:
                print(parking_lot[i][j].center(6) + "|", end="")
        print()


def main():
    lines = int(input("How many lines in the parking lot? "))
    cars_per_line = int(input("How many cars in each line? "))

    the_parking_lot = [[""] * cars_per_line for i in range(lines)]
    f_continue = True
    while f_continue:
        print("Choose one of the following options: ")
        print("1) Add car")
        print("2) Remove car")
        print("3) Print parking lot")
        print("0) Exit")

        choice = int(input("Enter your choice --> "))
        if choice == 1:
            car_number = input("Enter car number: ")
            res = park_car(the_parking_lot, car_number)
            if res:
                print("Car was parked successfully!")
            else:
                print("Parking lot is full!")

        elif choice == 2:
            car_number = input("Enter car number: ")
            res = remove_car(the_parking_lot, car_number)
            if res:
                print("Car was moved successfully!")
            else:
                print("Car is not in the parking lot!")

        elif choice == 3:
            print_parking_lot(the_parking_lot)
        elif choice == 0:
            f_continue = False
        else:
            print("Invalid option")
        print()
    print("Goodbye!")


if __name__ == "__main__":
    main()