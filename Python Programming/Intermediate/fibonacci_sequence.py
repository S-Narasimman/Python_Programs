def fibonacci_seq(terms):

    """
    This function takes in an integer as input and returns that
    number of digits of the fibonacci sequence in the form of a list.
    """
    try: # input validation
        terms = int(terms)
    except Exception as e: # catching exceptions
        return f"Please enter a valid integer > 0.\n{e}"

    fib = [0,1] # setting the default values
    if terms == 0: # returning message for 0 input
        return "Please enter a number greater than 0"
    elif terms==1: # 1 term
        return [0]
    elif terms==2: # 2 terms
        return fib
    else: # n terms
        i = 0 # setting iterable for exit
        while i<terms-2: # -2 because we already have 2 default values
            fib.append(fib[i]+fib[i+1]) # appending initial fib list
            i += 1 # increasing iterable by 1
        return fib # returning the updated fib list
    
if __name__=="__main__": # EXECUTION
    n = input("Enter the number of terms of the fibonacci sequence\nyou wish to print: ")
    print(fibonacci_seq(n))