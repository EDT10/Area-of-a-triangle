#header describing the program

print("###### THIS PROGRAM CALCULATES THE AREA OF A TRIANGE ######")


# a function that calculates the area of the triangle.

def cal():
    #ask for length and width of triangle
    length = input("Please enter the length: ")
    width = input("Please enter the width: ")

    # convert the string values to floats and calculate the total area of the triangle.
    total_area = float(length) * float(width)

    print(f"The area of the triangle is: {total_area}")


while True:
    #ask use if they a have a triangle to calculate. 
    new_cal = input("Do you have a triangle to calculate? Yes or No. ")

    #call the game function created above if user answered yes.
    if new_cal == "Yes" or new_cal == "yes":
        cal()
    
    #break out of while loop if user answered no
    elif new_cal == "No" or new_cal == "no":
        print("Thank you, Goodbye!")
        break

    #ask for a valid input if use does not enter yes or no value
    else:
        print("Incorrect input. Please enter a valid response.")
