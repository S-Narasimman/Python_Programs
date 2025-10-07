#Code to print the total sum of digits if input = 123
#Author: Narasimman
num = int(input('Enter Numbers: '))
num_str = str(num) #int cant be itterated so we changed the type to string here
sum_of_num = 0
for i in num_str:
  sum_of_num = sum_of_num + int(i) #here we changed the 'i' type to int becz in above step we changed it to 'string' for 'iteration'.But now we need 'int' type again to 'sum'
  print(sum_of_num)