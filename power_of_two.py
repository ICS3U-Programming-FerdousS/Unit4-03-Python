# Created by: Ferdous Sediqi
# Created on: April. 17 2022
# created by: Ferdous Sediqi
# Modified on: April 20, 2022
# This program asks the user to enter a number
# and then uses a do FOR loop to find the square of the numbers
# from 0 untill the user number

def main():
    # initialize the loop counter
    loop_counter = 0
    # get the user number as a string
    user_num_as_string = input("Enter a number: ")
    print("")

    try:
        # change input to int
        user_num_as_int = int(user_num_as_string)
        if user_num_as_int <= 0:
            print("Input was not a positive number.")
            exit()
        # for loop to find the square of the number
        for loop_counter in range(user_num_as_int + 1):
            print("Tracking {} times through loop.".format(loop_counter))
            loop_counter = loop_counter + 1
            power = loop_counter**2
            print("{}^2 = {}".format(loop_counter, power))
            print("")
            if loop_counter >= user_num_as_int:
                break

    # display invalid input
    except Exception:
        print("")
        print("Invalid input. Input is not an integer.")
        exit()


if __name__ == "__main__":
    main()
