# Check for Armstrong Number
# By Shantanu Das

def armstrong_number(number):
    
    """
    This function checks to see if a number is an armstrong number.
    It performs input validation and makes sure that only eligible
    integers make through.
    What is an Armstrong Number?
        - A number of n digits that is equal to the sum of of its
        digits, each raised to the power of n.
        153 = (1)^3 + (5)^3 + (3)^3
        9474 = (9)^4 + (4)^4 + (7)^4 + (4)^4
    """
    try: # Input validation. Making sure only integers make it through.
        number = int(number)
        if number >= 0: # Taking only positive integers
            num = number
        else: # ValueError for negative integers
            raise ValueError(f"{number} is not a valid input. Try positive int.")
    except Exception as e: # Error for invalid data type
        return f"{e}\n\nPlease enter a valid integer."
    
    num = number # Making a copy of the original input number
    digits = len(str(num))
    arm_num=0 # Setting the ticker to 0
    
    while num>0: # While loop for numbers greater than 0
        last_digit = num%10 # Extracting last digit
        arm_num += last_digit**digits # Adding cube of last digit to ticker
        num = (num-last_digit)//10 # Removing last digit from number
    
    if arm_num == number: # Checking to see if arm_num == number (Check for armstrong number)
        return f"{number} is an Armstrong number." # Returning affirmation
    else:
        return f"{number} is not an Armstrong number." # returning negation
    

if __name__=="__main__":
    n = input("Enter a number: ")
    print(armstrong_number(n))
