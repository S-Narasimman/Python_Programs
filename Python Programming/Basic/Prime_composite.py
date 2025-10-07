# Code to get input from user and check whether it is prime number or composite number using for loop
#Author: Narasimman
num = int(input('Enter Number to check prime or composite number: '))
count = 0
for i in range(2,num): #here we give 2as the initial number because all the number will divisible by 1.
  if num % i == 0:
    count += 1 #here we used '+= 1' to check the condition below
    break #after the condition meet loop gets break
  if count > 0:
    print('Composite Number!')
  else:
    print('Prime Number!')