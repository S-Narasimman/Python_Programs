# Sum of n digitis - Recursive approach
# By Shantanu Das

def sum_of_n(num):

    """
    Returns the sum of the first n number of digits provided.
    This function uses a recursive approach.
    """
    try: # input validation to make sure it is an int
        num=int(num) 
        if num<0: # making sure number of digits is positive
            return f"Please enter a prosive integer greater than 0.\n{num} is not a valid input."
        elif num==0: # input of 0 returns no count
            return 0
        else: # Recursive run
            return num + sum_of_n(num-1)

    except Exception as e: # Catching errors and displaying
        return f"Please provide a valid positive integer input greater than 0.\n\n{num} is an {e}"
    
if __name__=="__main__": # Execution
    n = input("Enter a number: ")
    print(sum_of_n(n))