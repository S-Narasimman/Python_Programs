# Palindrome Checker
#Author: Venkatesan
text = input("Enter a string or number: ")

# Reverse the string
if text == text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
