# Loop Based Addition
#Author: Venkatesan
n = int(input("How many numbers do you want to add? "))
total = 0

for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    total += num

print("Total sum:", total)
