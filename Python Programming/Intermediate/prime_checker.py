### PRIME NUMBER CHECKER FUNCTION - Faster###
# By Shantanu Das

def check_prime(num):

  """
  Takes in a number and checks if it is prime or not
  """
  num = abs(num) # Converting num to its absolute value (negative > positive)
  if num == 0 or num == 1: # default case
    return f'{num} is neither prime nor composite.'
  elif num == 2: # since 2 is a prime number
    return f'{num} is a prime number.'
  else: # main check case
    for i in range(2,int(num**0.5)+1):
      if num%i == 0: # Non-prime check only
        return f'{num} is a non-prime composite number'
    return f'{num} is a prime number.'


if __name__=="__main__": # Execution

  try: # Input validation
    number = int(input("Want to check if a number is prime?\nEnter the number: "))
    print(check_prime(number))

  except ValueError:
    print('Please enter a valid integer.')
