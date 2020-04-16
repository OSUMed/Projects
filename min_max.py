# Author: Srikanth Medicherla
# Date: 4/15/2020
# Description: Asks the user for for how many integers to enter and for the picked number be 1 or above.
#              Then it asks them to input them. Afterwards, it computes the minimum and maximum numbers
#              in the group of numbers the user inputted.

print("How many integers would you like to enter? ")
num = int(input())                                        # num means number
print("Please enter " + str(num) + " integers.")
minimum = 0
maximum = 0
if num > 1:                        # Code split: First is if user inputs an integer above 1, the next set is if they pick 1
    for a in range(1, num):
        current_num = int(input())  # current_num means current number
        if a == 1:                  # After assigning two more variables during first loop iteration, we can compute for min & max
            minimum = int(input())
            maximum = minimum
        if current_num < minimum:
            minimum = current_num
        if current_num > maximum:
            maximum = current_num
    print("min: " + str(minimum))
    print("max: " + str(maximum))

if num == int(1):                     # Code for if user chooses one for integer.
    minimum = int(input())
    maximum = minimum
    print("min: " + str(minimum))
    print("max: " + str(maximum))
