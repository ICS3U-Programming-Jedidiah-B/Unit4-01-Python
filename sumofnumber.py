#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Sept 2019
# Modified by: Ms Raffin
# Modified on: May 12, 2021
# Modified by: Jedidiah
# Modified on: April 20, 2022
# This program asks the user to enter a positive number
# and then uses a loop to calculate and display the sum
# of all numbers from 0 until that number.


def main():

    try:
        # initialize the loop counter and sum
        loop_counter = 0
        sum = 0

        # get the user number as a string
        user_number = int(input("Enter a positive number: "))
        print("")
        # to catch negative inputs
        if user_number < 0:
            print("please enter a postive integer")

        # calculate the sum of all numbers from 0 to user number
        while (loop_counter <= user_number):
            sum = sum + loop_counter
            print("Tracking {0} times through loop.".format(loop_counter))
            loop_counter = loop_counter + 1

            print("")
            print ("The sum of the numbers from 0 to {} is: {}.".format(
                user_number, sum))
    # error control
    except ValueError:
        print("{} is not a postive integer".format(user_number))
    finally:
        print("thanks for using this program")


if __name__ == "__main__":
    main()
