# Triangle using while loop
# By Shantanu Das

def triangle(base):

    """
    This function takes the size of the base of a triangle and draws it
    using the "*" character.
    """
    try: # Input validation
        base = int(base) # converting input to integer
        if base>0: # Validating positive input
            if base%2==0: # checking for even. Only odd required
                base += 1 # +1 if even
            else: # else no change
                base = base
            
            count = 1 # setting a counter to 1
            
            while count<=base: # running while loop
                space=int((base-count)/2)*" " # spaces
                star=count*"*" # stars
                print(f"{space}{star}") # Printing required output
                count += 2 # increasing count by 2
        else: # raising error for negative-integer input
            raise ValueError(f"Your input '{base}' is an invalid positive integer > 0.")

    except Exception as e: # raising error for non-integer input
        print(f"Error: please enter a valid integer > 0.\n{e}")


if __name__=="__main__": # Execution

    base = input("Enter the size of the triangle's base: ")
    triangle(base)

    