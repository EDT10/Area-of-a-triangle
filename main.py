# header describing the program

print("###### THIS PROGRAM CALCULATES THE AREA OF A TRIANGE ######")

# a function that calculates the area of the triangle.


def cal():
    # ask for length and width of triangle
    length = input("Please enter the length: ")
    width = input("Please enter the width: ")

    # Use try and except to handle errors
    try:
        # convert the string values to floats and calculate the total area of the triangle.
        total_area = float(length) * float(width)
    # create an exception for input that are not numbers and negative numbers. Prints out the error message
    except ValueError:
        print("ERR: Please enter a number")
    else:
        # if statement for handling negative numbers.
        if float(width) <= 0 or float(length) <= 0:
            print(f"ERR: Sorry, you can't input negative numbers.")
        else:
            print(f"The area of the triangle is: {total_area}")

# while loop to continue ask users for additional area to calculate.


while True:
    # ask use if they a have a triangle to calculate.
    new_cal = input("Do you have a triangle to calculate? Yes or No. ")


    # call the game function created above if user answered yes. Used the .lower() string method to convert user input to lower case.
    if new_cal.lower() == "yes":
        cal()

    # break out of while loop if user answered no. Used the .lower() string method to convert user input to lower case.
    elif new_cal.lower() == "no":
        print("Thank you, Goodbye!")
        break

    # ask for a valid input if use does not enter yes or no value
    else:
        print("Incorrect input. Please enter a valid response.")
