#find the factorial for the input
#Author: Narasimman
n = int(input('Enter number for factorial:'))
if n >= 0:
 total = 1
 for i in range(1,n+1):
   total = total * i
 print(total)
else:
 print('Enter number greater than 0!')