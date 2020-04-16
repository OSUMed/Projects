# Author: Srikanth Medicherla
# Date: 4/14/2020
# Description: A program designed to ask the user to enter a positive integer
#              and then print all the factors of that number in ascending order.

num = int(input("Please enter a positive integer: "))  # num means number
print("The factors of", num, "are:")
for a in range(1, num+1):                              # This format is used to print numbers in ascending order
    if num%a == 0:
        print(a)
