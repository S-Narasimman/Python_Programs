# Calculating the factorial of a number using Recursion
# By Shantanu Das

def factorial(num): #function definition

    """
    Takes in an integer and returns the factorial of it.
    Performs input validation and makes sure only integers
    are performed functions on.
    This method uses recursion.
    """

    try:
        num=int(num)
        if num<0:
            raise ValueError("Please enter a number greater than 0.")
        elif num==1 or num==0: # Exit condition
            return 1
        else:
            return num * factorial(num-1) # Recursive return
    except Exception as e:
        return f'Please enter a valid integer > 0.\n{e}'

    

    
# FOR EXECUTION
if __name__=="__main__":
    
    n = input("Enter a number: \n\n")
    print(factorial(n))
    
        