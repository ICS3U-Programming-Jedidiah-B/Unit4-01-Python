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
loop_counter = 0 
sum = 0 

def main():

  try:
     user_number = int(input("Enter a positive number: "))
     print("") 
     while (loop_counter <= user_number):
         sum = sum + loop_counter
         print("Tracking {0} times through loop.".format(loop_counter))
         loop_counter = loop_counter + 1
  except ValueError:
      print( "please enter an positive integer")
  else:
      print("")


if __name__ == "__main__":
    main()
